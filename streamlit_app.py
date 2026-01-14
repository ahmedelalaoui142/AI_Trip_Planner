import streamlit as st
import datetime
import requests
import sys

BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title= "Travel Planner Agentic Application",
    page_icon=":airplane:",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Travel Planner Agentic Application")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    

st.header("How can I help you in planning your trip? Let me know your destination.")

with st.form(key="query_form",clear_on_submit=True):
    user_input= st.text_input("User Input:",placeholder="ex: Plan a trip to Laayoune for 5 days...")
    submit_button= st.form_submit_button("Send")

if submit_button and user_input.strip():
    try:
        with st.spinner("Thinking..."):
            payload = {"query": user_input}
            response= requests.post(f"{BASE_URL}/query",json=payload)
        
        if response.status_code == 200:
            answer= response.json()["answer"]
            markdown_content= f"""# AI Travel Plan
            {answer}
            This is AI generated travel plan, please verify the information :)
            """
            st.markdown(markdown_content)
        else:
            st.error("Failed to respond: "+ response.text)
    except Exception as e:
        raise f"The response failed due to : {e}"