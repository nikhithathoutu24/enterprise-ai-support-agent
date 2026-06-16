import streamlit as st
from tools.agent_orchestrator import run_support_agent


st.set_page_config(
    page_title="Enterprise AI Support Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise AI Support Agent")
st.write("AI-powered support workflow using Llama, RAG, ChromaDB, customer lookup, and Jira automation.")

email = st.text_input("Customer Email", value="sarah@example.com")

message = st.text_area(
    "Support Message",
    value="My password reset email never arrives and I cannot access my account",
    height=120
)

if st.button("Run AI Support Agent"):
    with st.spinner("Agent is analyzing the support request..."):
        result = run_support_agent(email, message)

    ai = result["ai_classification"]
    customer = result["customer"]
    knowledge = result["knowledge_base"]
    jira = result["jira"]

    st.success("Support request processed successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("AI Classification")
        st.write(f"**Intent:** {ai['intent']}")
        st.write(f"**Priority:** {ai['priority']}")
        st.write(f"**Summary:** {ai['summary']}")
        st.write(f"**Requires Ticket:** {ai['requires_ticket']}")

    with col2:
        st.subheader("Customer Details")
        st.write(f"**Name:** {customer['name']}")
        st.write(f"**Company:** {customer['company']}")
        st.write(f"**Plan:** {customer['plan']}")
        st.write(f"**Account Status:** {customer['status']}")

    st.subheader("Knowledge Base Result")
    st.write(f"**Source:** {knowledge['source']}")
    st.info(knowledge["answer_context"])

    st.subheader("Jira Ticket")

    if jira and jira.get("created"):
        st.write(f"**Ticket ID:** {jira['ticket_id']}")
        st.write(f"**Ticket URL:** {jira['ticket_url']}")
        st.success(f"Jira ticket created: {jira['ticket_id']}")
    else:
        st.warning("No Jira ticket was created.")

    st.subheader("Final Response")
    st.write(
        f"Hi {customer['name']}, your request was classified as {ai['intent']}. "
        f"Summary: {ai['summary']}. "
        f"I found guidance from {knowledge['source']}."
    )
