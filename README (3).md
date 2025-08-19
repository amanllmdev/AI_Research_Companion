# 🧑‍🔬 AI Research Companion

AI Research Companion is an experimental project designed to assist in research workflows by integrating **CrewAI agents** with external APIs.  
It leverages **Mistral AI** for natural language processing tasks, enabling document analysis, semantic search, and intelligent query handling.

---

## 🚀 Features
- 📄 **PDF & Document Analysis** – Upload research papers and query their content.  
- 🤖 **CrewAI Integration** – Learn how to orchestrate multiple AI agents in research workflows.  
- 🔍 **Semantic Search** – Search through documents using embeddings and AI models.  
- ⚡ **Mistral AI Models** – Powered by Mistral AI API for performance and efficiency.  

---

## ⚠️ Important Notes
- This project uses the **Mistral AI API key** for inference.  
- Currently, it relies on the **free-tier version**, so you might experience **rate limit errors** if you run too many requests.  
- These issues will be addressed in future updates – for now, the goal is to **learn and experiment with CrewAI integrations**.  

---

## 🛠️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/AI_Research_Companion.git
   cd AI_Research_Companion
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your **Mistral AI API key** in a `.env` file:
   ```env
   MISTRAL_API_KEY=your_api_key_here
   ```

---

## ▶️ Usage

Run the application:
```bash
python main.py
```

Then follow the CLI/streamlit instructions to interact with the AI Research Companion.

---

## 📌 Roadmap
- ✅ Initial integration with CrewAI & Mistral AI  
- ⚡ Improve rate-limit handling  
- 📊 Add support for more APIs and embeddings  
- 🌐 Web-based UI  

---

## 🤝 Contributing
This project is mainly for **learning purposes**, but contributions are welcome.  
Feel free to open issues or submit PRs with improvements.  

---

## 📄 License
MIT License – free to use and modify.  
