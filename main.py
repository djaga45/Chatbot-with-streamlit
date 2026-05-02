import os


from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("Basic Chatbot with Streamlit")



## now we are starting with the chatbot development

if "chat_hist" not in st.session_state:
    st.session_state.chat_hist =[]


for message in st.session_state.chat_hist:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


##llm iniate

llm=ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0.3,
)

##nput

user_prompt= st.chat_input("Ask Chatbot....")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_hist.append({"role":"user", "content":user_prompt})


    response=llm.invoke(
        input=[{"role": "system", "content": "You are a helpfull assistant"}, *st.session_state.chat_hist]
    )

    assistant_response=response.content
    st.session_state.chat_hist.append({"role":"assistant", "content":assistant_response})


    with st.chat_message("assistant"):
        st.markdown(assistant_response)






