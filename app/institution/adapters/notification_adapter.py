from __future__ import annotations

from app.institution.adapters.base import BaseWorkflowAdapter, WorkflowExecutionContext, WorkflowResult


class NotificationAdapter(BaseWorkflowAdapter):
    """
    Adapter for the Notification Engine.

    Supports email, SMS, push notifications,
    WhatsApp, Slack and future channels.
    """

    def send_email(
        self,
        context: WorkflowExecutionContext,
        subject: str,
        body: str,
    ) -> WorkflowResult:
        return self.build_result(
            "notification.email.sent",
            data={
                "workflow_id": context.workflow_id,
                "execution_id": context.execution_id,
                "subject": subject,
                "body": body,
            },
        )

    def send_sms(
        self,
        context: WorkflowExecutionContext,
        message: str,
    ) -> WorkflowResult:
        return self.build_result(
            "notification.sms.sent",
            data={
                "workflow_id": context.workflow_id,
                "execution_id": context.execution_id,
                "message": message,
            },
        )

    def send_push(
        self,
        context: WorkflowExecutionContext,
        title: str,
        message: str,
    ) -> WorkflowResult:
        return self.build_result(
            "notification.push.sent",
            data={
                "workflow_id": context.workflow_id,
                "execution_id": context.execution_id,
                "title": title,
                "message": message,
            },
        )

    def broadcast(
        self,
        context: WorkflowExecutionContext,
        event: str,
        payload: dict,
    ) -> WorkflowResult:
        return self.build_result(
            event,
            data={
                "workflow_id": context.workflow_id,
                "execution_id": context.execution_id,
                "payload": payload,
            },
        )