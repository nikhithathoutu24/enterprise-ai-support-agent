from fastapi import FastAPI
from pydantic import BaseModel

from tools.salesforce_tool import get_customer_details
from tools.jira_tool import create_jira_ticket
from tools.ollama_tool import classify_with_llama


app = FastAPI()


class SupportMessage(BaseModel):
    email: str
    message: str


def generate_response(ai_result: dict, customer: dict, jira_result: dict):
    name = customer["name"]
    intent = ai_result["intent"]
    summary = ai_result["summary"]

    if jira_result and jira_result.get("created"):
        ticket_text = f" A Jira ticket has been created: {jira_result['ticket_id']}."
    else:
        ticket_text = " No Jira ticket was created."

    return f"Hi {name}, your request was classified as {intent}. Summary: {summary}.{ticket_text}"


@app.get("/")
def home():
    return {"status": "AI Support Agent is running with local Llama"}


@app.post("/support")
def support_agent(input_data: SupportMessage):
    user_email = input_data.email
    user_message = input_data.message

    ai_result = classify_with_llama(user_message)
    customer = get_customer_details(user_email)

    jira_result = None
    if ai_result.get("requires_ticket"):
        jira_result = create_jira_ticket(
            customer,
            ai_result["intent"],
            ai_result["summary"]
        )

    response = generate_response(ai_result, customer, jira_result)

    return {
        "input": {
            "email": user_email,
            "message": user_message
        },
        "ai_classification": ai_result,
        "customer": customer,
        "jira": jira_result,
        "output": response
    }
