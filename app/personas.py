def detect_persona(message):
    message = message.lower()

    # Angry Customer
    if any(word in message for word in [
        "angry",
        "frustrated",
        "terrible",
        "worst",
        "bad service",
        "complaint"
    ]):
        return "angry"

    # Professional Customer
    if any(word in message for word in [
        "please",
        "kindly",
        "thank you",
        "would like"
    ]):
        return "professional"

    # Premium Customer
    if any(word in message for word in [
        "premium",
        "vip",
        "membership"
    ]):
        return "premium"

    # New Customer
    if any(word in message for word in [
        "first time",
        "new customer",
        "new user"
    ]):
        return "new_customer"

    # Default
    return "friendly"


def get_system_prompt(persona):

    prompts = {

        "friendly": """
You are a friendly customer support agent.
Be warm, polite, and helpful.
Provide clear answers.
""",

        "professional": """
You are a professional customer support representative.
Be concise, formal, and professional.
Provide accurate information.
""",

        "angry": """
The customer is frustrated or upset.
Start by showing empathy.
Acknowledge their concern.
Then provide a solution in a calm and respectful manner.
""",

        "premium": """
You are assisting a premium customer.
Provide priority support.
Be highly attentive, professional, and personalized.
Make the customer feel valued.
""",

        "new_customer": """
You are assisting a first-time customer.
Explain policies clearly and patiently.
Avoid technical jargon.
Guide the customer step by step.
"""
    }

    return prompts.get(persona, prompts["friendly"])