import os

import requests
from django.conf import settings


class ChatwootClient:
    def __post__(self, url: str, payload: dict):
        try:
            requests.post(
                json=payload,
                headers={
                    "accept": "json",
                    "api_access_token": os.environ.get("AGENT_BOT_TOKEN"),
                },
                url=f"{settings.CHATWOOT_URL}/{url}",
            )
        except Exception as e:
            print(f"URL Exception: #{e}")

    def send_message(self, account, conversation, message):
        return self.__post__(
            f"api/v1/accounts/{account}/conversations/{conversation}/messages",
            {"content": message},
        )

    def send_options_message(self, account, conversation, message, items):
        return self.__post__(
            f"api/v1/accounts/{account}/conversations/{conversation}/messages",
            {
                "content": message,
                "content_type": "input_select",
                "content_attributes": {"items": items},
            },
        )

    def send_form_message(self, account, conversation, message, items):
        return self.__post__(
            f"api/v1/accounts/{account}/conversations/{conversation}/messages",
            {
                "content": message,
                "content_type": "form",
                "content_attributes": {"items": items},
            },
        )

    def send_cards_message(self, account, conversation, message, items):
        return self.__post__(
            f"api/v1/accounts/{account}/conversations/{conversation}/messages",
            {
                "content": message,
                "content_type": "cards",
                "content_attributes": {"items": items},
            },
        )

    def handoff_conversation(self, account, conversation, status="open"):
        return self.__post__(
            f"api/v1/accounts/{account}/conversations/{conversation}/toggle_status",
            {"status": status},
        )
