from openai import OpenAI
import streamlit as st
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv


load_dotenv() 
with st.sidebar:
    gemini_api_key = ${{ secrets.gemini_api_key }}
    

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Gemini")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not gemini_api_key:
        st.info("Please add your Gemini API key to continue.")
        st.stop()

    # client = OpenAI(api_key=openai_api_key)
    # 
    # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    # msg = response.choices[0].message.content
    # st.session_state.messages.append({"role": "assistant", "content": msg})
    # st.chat_message("assistant").write(msg)

    genai.configure(api_key= gemini_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    platform = ["Twitter", "Linkedin", "Blog"]

    contents = [f"Create a concise and engaging Twitter thread about '{prompt}'. Keep it within Twitter's character limits and use relevant hashtags and emojis.", f"Create a LinkedIn post on '{prompt}' in a professional tone. Provide insights and key takeaways for business professionals.",
            f"Write a blog post on '{prompt}' with an introduction, key points, and a conclusion. Make it informative and engaging."]
    
   
    model = genai.GenerativeModel("gemini-1.5-flash")
    for i in range(3):
        
        response = model.generate_content(contents[i])
        msg = response.text

        st.chat_message("assistant").write(msg)

        


