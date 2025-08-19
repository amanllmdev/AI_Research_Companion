import asyncio

# Fix for "no current event loop" in Streamlit
try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

import streamlit as st
from agents_runner import run_agents
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
hf_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not hf_key:
    st.error("❌ HUGGINGFACE_ACCESS_TOKEN not found in .env file.")
    st.stop()

# Streamlit Page Config
st.set_page_config(page_title="AI Research Paper Companion", layout="centered")
st.title("📄 AI Research Paper Companion")

# Upload PDF
uploaded_file = st.file_uploader("Upload a research paper (PDF)", type="pdf")

if uploaded_file:
    # Save the uploaded PDF
    with open("paper.pdf", "wb") as f:
        f.write(uploaded_file.read())

    if st.button("🔍 Analyze Paper"):
        with st.spinner("Running AI agents..."):
            output = run_agents()
        st.success("✅ Done!")
        st.write("### 🔬 Analysis Result")
        st.markdown(output)
