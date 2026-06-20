def needs_escalation(message):

    escalation_keywords = [
        "lawyer",
        "legal",
        "court",
        "sue",
        "manager",
        "human agent"
    ]

    return any(
        word in message.lower()
        for word in escalation_keywords
    )