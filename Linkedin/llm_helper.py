from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192"  # ✅ Correct model name
)

if __name__ == "__main__":
    response = llm.invoke("what are the two main ingredients in samosa")
    print(response.content)
