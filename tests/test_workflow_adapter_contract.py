from app.institution.adapters import (
    AustinAdapter,
    CommunityAdapter,
    CurrencyAdapter,
    GeoAdapter,
    NotificationAdapter,
    ProjectAdapter,
)
from app.institution.adapters.base import WorkflowExecutionContext, WorkflowResult


def test_workflow_adapters_return_standard_result():
    context = WorkflowExecutionContext(
        workflow_id="wf-institution-onboarding",
        execution_id="exec-101",
        variables={"institution_id": "inst-123"},
        metadata={"event": "institution.created"},
    )

    austin = AustinAdapter()
    austin_result = austin.recommend(context, "institution")
    assert isinstance(austin_result, WorkflowResult)
    assert austin_result.status == "completed"
    assert "recommendation" in austin_result.data

    notifications = NotificationAdapter()
    notification_result = notifications.send_email(
        context,
        subject="Welcome",
        body="Your institution is ready.",
    )
    assert isinstance(notification_result, WorkflowResult)
    assert notification_result.status == "completed"
    assert notification_result.event == "notification.email.sent"

    community = CommunityAdapter()
    community_result = community.moderate(context, "institution")
    assert isinstance(community_result, WorkflowResult)
    assert community_result.status == "completed"

    project = ProjectAdapter()
    project_result = project.create(context, {"name": "Sample Project"})
    assert isinstance(project_result, WorkflowResult)
    assert project_result.status == "completed"

    geo = GeoAdapter()
    geo_result = geo.resolve(context, "Victoria Island, Lagos")
    assert isinstance(geo_result, WorkflowResult)
    assert geo_result.status == "completed"

    currency = CurrencyAdapter()
    currency_result = currency.normalize(context, "ngn")
    assert isinstance(currency_result, WorkflowResult)
    assert currency_result.status == "completed"
    assert currency_result.data["currency"] == "NGN"
