from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from app.personas import detect_persona
from app.personas import get_system_prompt
from app.escalation import needs_escalation

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def get_answer(query):

    if needs_escalation(query):
        return "This query has been escalated to a human support agent."

    persona = detect_persona(query)

    docs = db.similarity_search(query, k=2)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    {get_system_prompt(persona)}

    Context:
    {context}

    User Question:
    {query}

    Answer:
    """

    response = llm.invoke(prompt)

    return response.content

