import streamlit as st
import dotenv
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")
import zipfile

st.set_page_config(page_title = "AI Website Creation", page_icon = "📰")

st.title("AI AUTOMATION WEBSITE CREATION")

prompt = st.text_area("Write here about the website you want to create:")

if st.button("Generate Website"):
    message = [("system", """You are a expert in web development creating professional.
                so create html, css, javascript code for creating a frontend based on user prompt.
                
                the output should be only contain clean code in the below format:
                
                --html--
                <html code>
                --html--
                
                --css--
                <css code>  
                --css--
                
                --javascript--
                <javascript code>
                --javascript--"""
                )]
    message.append(("user", prompt))

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

    response = model.invoke(message)

    with open("index.html", "w",) as file:
        file.write(response.content.split("--html--")[1].strip())

    with open("style.css", "w",) as file:
        file.write(response.content.split("--css--")[1].strip())

    with open("script.js", "w",) as file:
        file.write(response.content.split("--javascript--")[1].strip())

    with zipfile.ZipFile("website.zip", "w") as zip:
        zip.write("index.html")
        zip.write("style.css")
        zip.write("script.js")
    
    st.download_button("Click to Download", 
                        data=open("website.zip", "rb"), 
                        file_name="website.zip")

    st.write("success")