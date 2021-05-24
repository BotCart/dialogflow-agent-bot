import os

from google.cloud import dialogflow_v2beta1 as dialogflow


# noinspection PyTypeChecker
class DialogflowClient:
    def get_response(self, session_id: str, content: str):
        return self.detect_intent_knowledge(
            text=content,
            session_id=session_id,
            project_id=os.environ.get("DIALOGFLOW_PROJECT_ID"),
            knowledge_base_id=os.environ.get("DIALOGFLOW_KNOWLEDGE_BASE_ID"),
        )

    def detect_intent_knowledge(
        self,
        text: str,
        session_id: str,
        project_id: str,
        knowledge_base_id: str,
        language_code: str = "en-US",
    ):
        """Returns the result of detect intent with querying Knowledge Connector.

        Args:
        text: Queries to send.
        session_id: Id of the session, using the same `session_id` between requests
                  allows continuation of the conversation.
        project_id: The GCP project linked with the agent you are going to query.
        knowledge_base_id: The Knowledge base's id to query against.
        language_code: Language of the queries.

        Return:
        fulfillment_text
        """
        session_client = dialogflow.SessionsClient()
        session_path = session_client.session_path(project_id, session_id)

        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        knowledge_base_path = dialogflow.KnowledgeBasesClient.knowledge_base_path(
            project_id, knowledge_base_id
        )

        query_params = dialogflow.QueryParameters(
            knowledge_base_names=[knowledge_base_path]
        )

        request = dialogflow.DetectIntentRequest(
            session=session_path, query_input=query_input, query_params=query_params
        )

        response = session_client.detect_intent(request=request)
        return response.query_result.fulfillment_text
