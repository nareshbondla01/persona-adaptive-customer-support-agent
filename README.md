# Persona-Adaptive Customer Support Agent

## Project Overview

Customer support systems often struggle to provide personalized responses while also following company policies accurately. Generic chatbots may generate responses that sound natural but sometimes provide incorrect information because they do not have access to company-specific knowledge.

This project addresses that challenge by combining three important concepts:

1. Persona-Aware Response Generation
2. Retrieval-Augmented Generation (RAG)
3. Human Escalation Mechanism

The application identifies the type of customer interacting with the system, retrieves relevant company information from an internal knowledge base, and generates responses using a Large Language Model. For sensitive situations such as legal complaints or requests for human intervention, the system immediately escalates the conversation instead of generating an automated response.

The final solution is presented through a Streamlit-based web interface that allows users to interact with the support assistant in real time.

---

# Problem Statement

Traditional customer support chatbots face two common issues:

* They provide the same style of response to every customer regardless of their situation.
* They may generate inaccurate answers when company-specific information is not available.

For example:

* An angry customer expects empathy and reassurance.
* A premium customer expects priority assistance.
* A first-time customer may require detailed guidance.

At the same time, the system must answer questions using official company policies rather than relying solely on the language model's general knowledge.

This project was developed to solve these challenges.

---

# Objectives

The primary objectives of this project are:

* Understand different customer personas.
* Adapt responses according to customer behavior and intent.
* Retrieve information from a company knowledge repository.
* Generate context-aware responses using an LLM.
* Escalate sensitive conversations to human support representatives.
* Provide a simple web-based interface for interaction.

---

# System Workflow

The complete workflow of the application is shown below:

User Query

↓

Persona Identification

↓

Escalation Check

↓

Knowledge Retrieval

↓

Relevant Policy Extraction

↓

Language Model Response Generation

↓

Final Response

---

# Persona Adaptation

One of the key features of this project is persona adaptation.

Instead of responding to every customer in the same way, the system first identifies the user's communication style and then adjusts its response strategy.

### Supported Personas

#### Friendly Customer

The system provides warm and helpful responses.

Example:

"Can I get a refund?"

Response style:

Friendly and conversational.

---

#### Professional Customer

The system provides concise and formal responses.

Example:

"Please provide details regarding your refund policy."

Response style:

Professional and structured.

---

#### Angry Customer

The system begins by acknowledging the customer's frustration before providing assistance.

Example:

"I am frustrated with your terrible service."

Response style:

Empathetic and solution-oriented.

---

#### Premium Customer

The system provides priority-style support and personalized assistance.

Example:

"I am a premium member."

Response style:

High-priority and customer-focused.

---

#### New Customer

The system provides detailed guidance and avoids technical terminology.

Example:

"I am a new customer. How does shipping work?"

Response style:

Educational and supportive.

---

# Retrieval-Augmented Generation (RAG)

Large Language Models are powerful, but they do not automatically know company-specific policies.

To solve this problem, Retrieval-Augmented Generation (RAG) is implemented.

The system stores company information in text documents and retrieves the most relevant information before generating a response.

Instead of relying only on the model's training data, the assistant uses retrieved company knowledge to answer questions accurately.

---

# Knowledge Base

The knowledge repository currently contains information related to:

* Refund Policy
* Shipping Policy
* Billing Information
* Account Assistance
* Subscription Management
* Product Returns
* Premium Membership Benefits
* Delivery Delays
* Technical Support
* Contact Information
* Privacy Policy
* Discount Programs
* Warranty Information
* Order Cancellation Rules

These documents act as the organization's internal knowledge source.

---

# Vector Database Implementation

To efficiently search large amounts of information, a vector database is used.

### Why a Vector Database?

If the number of policy documents grows from a few files to hundreds or thousands of files, searching through every document becomes inefficient.

To solve this issue:

1. Documents are converted into embeddings.
2. Embeddings are stored inside FAISS.
3. User queries are converted into embeddings.
4. Similarity search retrieves the most relevant information.

This allows the system to quickly locate relevant knowledge without scanning every document.

---

# Human Escalation Mechanism

Certain situations should not be handled by an automated assistant.

The project includes an escalation layer that detects high-risk conversations.

Examples include:

* Legal threats
* Requests for managers
* Court-related discussions
* Requests for human representatives

When such situations are detected, the system bypasses automated response generation and routes the conversation for human assistance.

Example:

User:

"I want to sue this company."

Response:

"This query has been escalated to a human support agent."

---

# Technologies Used

### Programming Language

* Python

### User Interface

* Streamlit

### Language Model

* Llama 3.3 70B (Groq)

### Retrieval Framework

* LangChain

### Embedding Model

* Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* FAISS

### Environment Management

* Python Dotenv

---

# Project Structure

AIASSISTENT/

├── app/

│ ├── chatbot.py

│ ├── rag.py

│ ├── personas.py

│ └── escalation.py

│

├── data/

│ ├── policy files

│ └── support knowledge documents

│

├── faiss_index/

├── ui.py

├── .env

└── README.md

---

# Sample Questions

### Policy Questions

* How long does shipping take?
* Can I get a refund?
* What is your warranty policy?
* What benefits do premium members receive?
* How do you protect customer data?

### Persona Questions

* I am frustrated with your terrible service.
* Please explain your refund policy.
* I am a premium member.
* I am a new customer.

### Escalation Questions

* I want to sue this company.
* Connect me to a human representative.
* I need to speak with a manager.

---

# Future Enhancements

The current implementation serves as a functional prototype. Future improvements may include:

* Sentiment analysis using dedicated models
* Customer conversation history
* Ticket generation system
* Multi-language support
* Customer authentication
* Analytics dashboard
* Database-backed knowledge management

---

# Conclusion

This project demonstrates how Retrieval-Augmented Generation, persona adaptation, and human escalation can be combined to create a more reliable and customer-centric support system.

By retrieving verified company information, adapting responses to different customer types, and recognizing situations that require human involvement, the system provides a practical foundation for modern AI-assisted customer support.
