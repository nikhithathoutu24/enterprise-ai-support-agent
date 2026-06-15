from fastapi import FastAPI
from pydantic import BaseModel

from tools.salesforce_tool import get_customer_details
from tools.jira_tool import create_jira_ticket


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


def generate_response(intent: str, customer: dict, jira_result: dict):
    name = customer["name"]

    if jira_result["created"]:
        ticket_text = f" A Jira ticket has been created: {jira_result['ticket_id']}."
    else:
        ticket_text = " I could not create a Jira ticket."

    if intent == "login_issue":
        return f"Hi {name}, your login issue has been reviewed.{ticket_text}"
    elif intent == "billing_issue":
        return f"Hi {name}, your billing issue has been routed to support.{ticket_text}"
    elif intent == "bug_report":
        return f"Hi {name}, your bug report has been sent to engineering.{ticket_text}"
    elif intent == "feature_request":
        return f"Hi {name}, your feature request has been shared with the product team.{ticket_text}"
    else:
        return f"Hi {name}, your support request has been received.{ticket_text}"


@app.get("/")
def home():
    return {"status": "AI Support Agent is running"}


@app.post("/support")
def support_agent(input_data: SupportMessage):
    user_email = input_data.email
    user_message = input_data.message

    intent = classify_intent(user_message)
    customer = get_customer_details(user_email)
    jira_result = create_jira_ticket(customer, intent, user_message)
    response = generate_response(intent, customer, jira_result)

    return {
        "input": {
            "email": user_email,
            "message": user_message
        },
        "intent": intent,
        "customer": customer,
        "jira": jira_result,
        "output": response
    }
