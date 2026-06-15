from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class SupportMessage(BaseModel):
    message: str


def classify_intent(message: str):
    message = message.lower()

    if "login" in message or "locked" in message or "password" in message:
        return "login_issue"

    elif "payment" in message or "billing" in message or "invoice" in message:
        return "billing_issue"

    elif "bug" in message or "error" in message or "not working" in message:
        return "bug_report"

    elif "feature" in message or "request" in message:
        return "feature_request"

    else:
        return "general_support"


@app.get("/")
def home():
    return {"status": "AI Support Agent is running"}


@app.post("/support")
def support_agent(input_data: SupportMessage):
    user_message = input_data.message
    intent = classify_intent(user_message)

    return {
        "input": user_message,
        "intent": intent,
        "output": f"Your issue has been classified as: {intent}"
    }