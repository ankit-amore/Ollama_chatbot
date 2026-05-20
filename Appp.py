import streamlit as st                                                                             
from ollama import Client

# create client instance (VERY IMPORTANT)
client = Client(host="http://localhost:11434")
st.set_page_config(
    page_title="Custom LLM model by Ankita More - Ollama ",
    layout="centered"  
)

st.title("miss. Ankita More - Ollama App")

prompt = st.text_area("Enter your prompt:", height=100)

if st.button("Genarate Response"):
    if prompt.strip("gemma:2b") == "":
        st.warning("please enter a prompt.")
    else:
        
        with st.spinner("thinking..."):
            response = client.chat(
                model="gemma:2b",     #kimi-k2.5:cloud
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            
            st.success("Response Generated!")
            st.write(response["message"]["content"])