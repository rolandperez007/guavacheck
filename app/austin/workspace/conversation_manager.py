"""
Austin Conversation Manager

Controls every Austin chat session.

Responsibilities

• create conversations
• archive conversations
• restore sessions
• manage history
• streaming responses
• attachments
• voice sessions
• institution conversations
• property conversations
"""

from uuid import uuid4
from datetime import datetime


class ConversationManager:

    def create(self, user_id: str):

        return {
            "conversation_id": str(uuid4()),
            "user_id": user_id,
            "created_at": datetime.utcnow(),
            "messages": [],
            "context": {},
        }

    def archive(self, conversation):
        conversation["archived"] = True
        return conversation

    def restore(self, conversation):
        conversation["archived"] = False
        return conversation

    def append_message(self, conversation, role, content):

        conversation["messages"].append({
            "role": role,
            "content": content,
            "timestamp": datetime.utcnow(),
        })

        return conversation