from fastapi import Request


def normalize_request(request: Request, body: dict | None) -> dict:
    if body is None:
        body = {}

    path = request.url.path

    action = body.get("action")

    if not action:
        if body.get("query") or body.get("message"):
            action = "run_job"
        elif path.startswith("/ws"):
            action = "ws_message"
        else:
            action = "api_call"

    if isinstance(body.get("payload"), dict):
        payload = body["payload"]
    elif "query" in body:
        payload = {"query": body["query"]}
    elif "message" in body:
        payload = {"message": body["message"]}
    else:
        payload = body

    user_id = (
        body.get("user_id")
        or request.headers.get("x-user-id")
        or request.headers.get("user-id")
    )

    return {
        "query": payload.get("query") if isinstance(payload, dict) else None,
        "action": action,
        "payload": payload,
        "user_id": user_id,
        "path": path,
        "method": request.method,
        "headers": dict(request.headers),
    }
