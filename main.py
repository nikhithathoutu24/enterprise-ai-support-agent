from fastapi import FastAPI
from pydantic import BaseModel

from tools.salesforce_tool import get_customer_details


app = FastAPI()


class SupportMessage(BaseModel):
    email: str
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


def generate_response(intent: str, customer: dict):
    name = customer["name"]
    status = customer["status"]
    plan = customer["plan"]

    if intent == "login_issue":
        if status == "locked":
            return f"Hi {name}, your account appears to be locked. Please reset your password or contact support to unlock your account."
        elif status == "active":
            return f"Hi {name}, your account is active. Please try resetting your password and clearing your browser cache."
        else:
            return "We could not find your account details. Please verify your registered email address."

    elif intent == "billing_issue":
        return f"Hi {name}, I see you are on the {plan} plan. I will route your billing issue to the billing support team."

    elif intent == "bug_report":
        return f"Hi {name}, thank you for reporting this issue. I will create a technical support ticket for further investigation."

    elif intent == "feature_request":
        return f"Hi {name}, thank you for your feature request. I will forward this to the product team."

    else:
        return f"Hi {name}, thank you for contacting support. Our team will review your request."


@app.get("/")
def home():
    return {"status": "AI Support Agent is running"}


@app.post("/support")
def support_agent(input_data: SupportMessage):
    user_email = input_data.email
    user_message = input_data.message

    intent = classify_intent(user_message)
    customer = get_customer_details(user_email)
    response = generate_response(intent, customer)

    return {
        "input": {
            "email": user_email,
            "message": user_message
        },
        "intent": intent,
        "customer": customer,
        "output": response
    }
