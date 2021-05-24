from services.chatwoot_client import ChatwootClient
from services.dialogflow_client import DialogflowClient


class RequestHandler:
    handoff_message = (
        "Transferring the conversation to an agent. You will get a response shortly."
    )

    def __init__(self, params: dict):
        self.params = params
        self.event = params.get("event")
        if params.get("account"):
            self.account_id = params.get("account").get("id")
        if params.get("conversation"):
            self.conversation_id = params.get("conversation").get("id")

    def __handle_event__(self):
        if self.event == "message_created":
            if (
                self.params["message_type"] == "incoming"
                and self.params["conversation"]["status"] == "bot"
            ):
                self.__handle_message_created__()

        elif self.event == "message_updated":
            self.__handle_message_updated__()

        else:
            print(f"{self.event} Event not handled")

    def __handle_message_created__(self):
        source_id = self.params["conversation"]["contact_inbox"]["source_id"]
        self.__send_response_for_content__(source_id, self.params.get("content"))

    def __send_response_for_content__(self, source_id: str, content: str):
        chatwoot_client = ChatwootClient()
        dialogflow_client = DialogflowClient()

        message = dialogflow_client.get_response(session_id=source_id, content=content)

        if message == "__handoff__":
            chatwoot_client.send_message(
                account=self.account_id,
                conversation=self.conversation_id,
                message=self.handoff_message,
            )
            chatwoot_client.handoff_conversation(
                account=self.account_id, conversation=self.conversation_id
            )

        else:
            chatwoot_client.send_message(
                account=self.account_id,
                conversation=self.conversation_id,
                message=message,
            )

    # TODO: Need to Update
    def __handle_message_updated__(self):
        pass

    def process(self):
        self.__handle_event__()
