import os
import streamlit as st
import requests
import uuid
import time

st.title("Mental Healthcare Chatbot")
st.markdown("Hello! I'm your friendly mental health care assistant.")

REST_API_URL = os.getenv("REST_API_URL", 'localhost:5050')

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

user_input = st.text_input("You:", "")

if st.button("Send"):
    with st.spinner("Thinking..."):
        payload = {
            "session_id": st.session_state["session_id"],
            "prompt": user_input
        } 
        api_url = f"http://{REST_API_URL}/publish"
        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            # Poll for a response for up to 30 seconds
            response_url = f"http://{REST_API_URL}/response/{st.session_state.session_id}"
            backend_response = None
            start_time = time.time()

            while time.time() - start_time < 30:
                resp_check = requests.get(response_url)
                if resp_check.status_code == 200:
                    backend_response = resp_check.json().get("response")
                    break
                time.sleep(0.5)

            if backend_response:
                st.markdown(f"**Assistant:** {backend_response}")
            else:
                st.error("Error: No response received in time.")
        else:
            st.error("Error: Unable to process your request.")
