import os
from dotenv import load_dotenv
from crewai import Agent
from crewai_tools import PDFSearchTool
from litellm import completion

# Load env vars
load_dotenv()

# Set Mistral API key from environment (more secure)
if not os.getenv("MISTRAL_API_KEY"):
    os.environ["MISTRAL_API_KEY"] = "gBXNnc4RXZlQUNmE10sjuaKxFZbRXUho"

# 1. Wrapper around litellm.completion to behave like an LLM
class LiteLLMWrapper:
    def __init__(self, model="mistral/mistral-tiny"):
        self.model = model

    def __call__(self, prompt, **kwargs):
        try:
            # Ensures CrewAI can call it like a function
            resp = completion(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return resp["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error in LLM call: {e}")
            return f"Error: {str(e)}"

# Use Mistral tiny via LiteLLM
llm = LiteLLMWrapper(model="mistral/mistral-tiny")

# 2. FIXED: Use compatible embedding model and simpler config
rag_tool_config = {
    "llm": {
        "provider": "litellm",  # Use litellm instead of mistralai
        "config": {
            "model": "mistral/mistral-tiny",
            "api_key": os.getenv("MISTRAL_API_KEY")
        },
    },
    "embedder": {
        "provider": "huggingface",
        "config": {
            # Use a more compatible embedding model
            "model": "sentence-transformers/all-mpnet-base-v2",  # Changed from all-MiniLM-L6-v2
            # Remove API key for embeddings - usually not needed for sentence-transformers
        },
    },
}

# 3. ALTERNATIVE: Try without custom config first (most stable)
def create_pdf_tool():
    try:
        # Method 1: Try with default config (most stable)
        print("Trying default PDF tool configuration...")
        return PDFSearchTool(pdf="paper.pdf")
        
    except Exception as e1:
        print(f"Default config failed: {e1}")
        try:
            # Method 2: Try with simplified config
            print("Trying simplified config...")
            simple_config = {
                "embedder": {
                    "provider": "huggingface",
                    "config": {
                        "model": "sentence-transformers/all-mpnet-base-v2"
                    }
                }
            }
            return PDFSearchTool(pdf="paper.pdf", config=simple_config)
            
        except Exception as e2:
            print(f"Simplified config failed: {e2}")
            # Method 3: Force recreation with basic setup
            return PDFSearchTool(pdf="paper.pdf")

# Initialize PDF tool
pdf_tool = create_pdf_tool()

# 4. Define Agents using LiteLLM with error handling
try:
    explainer = Agent(
        role="Topic Explainer",
        goal="Explain complex technical ideas in simple terms",
        backstory="An expert science communicator and educator",
        tools=[pdf_tool],
        verbose=True,
        llm=llm
    )

    literature_agent = Agent(
        role="Literature Finder",
        goal="Find related works or previously published research",
        backstory="A research librarian skilled at academic literature discovery",
        tools=[pdf_tool],
        verbose=True,
        llm=llm
    )

    gap_analyzer = Agent(
        role="Gap Analyzer",
        goal="Identify research gaps or open questions in the paper",
        backstory="A critical analyst with a deep understanding of scientific research",
        tools=[pdf_tool],
        verbose=True,
        llm=llm
    )
except Exception as e:
    print(f"Error creating agents: {e}")
    raise