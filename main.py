from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SupportMessage(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AI Support Agent is running"}

@app.post("/support")
def support_agent(input_data: SupportMessage):
    user_message = input_data.message

    return {
        "input": user_message,
        "output": f"I received your support message: {user_message}"
    }