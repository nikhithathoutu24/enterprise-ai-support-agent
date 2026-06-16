from tools.ollama_tool import classify_with_llama
from tools.rag_tool import search_knowledge_base
from tools.salesforce_tool import get_customer_details
from tools.jira_tool import create_jira_ticket


def run_support_agent(email: str, message: str):
    """
    Agentic workflow:
    1. Classify message using local Llama
    2. Retrieve customer context
    3. Search knowledge base using ChromaDB
    4. Decide whether Jira ticket is needed
    5. Create Jira ticket if required
    """

    ai_result = classify_with_llama(message)
    customer = get_customer_details(email)
    knowledge = search_knowledge_base(message)

    jira_result = None

    if ai_result.get("requires_ticket"):
        jira_result = create_jira_ticket(
            customer,
            ai_result["intent"],
            f"{ai_result['summary']}\n\nKnowledge Base Context:\n{knowledge['answer_context']}"
        )

    return {
        "ai_classification": ai_result,
        "customer": customer,
        "knowledge_base": knowledge,
        "jira": jira_result
    }
