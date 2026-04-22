import json
import re

# Load knowledge base
with open("knowledge_base.json", "r", encoding="utf-8") as f:
    kb = json.load(f)

# Simple memory / state
state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "lead_capture_started": False
}


def mock_lead_capture(name, email, platform):
    print(f"\nLead captured successfully: {name}, {email}, {platform}\n")


def detect_intent(user_input: str) -> str:
    text = user_input.lower().strip()

    greeting_words = ["hi", "hello", "hey", "good morning", "good evening"]
    pricing_words = ["price", "pricing", "plan", "plans", "cost", "feature", "features", "refund", "support"]
    high_intent_words = ["sign up", "signup", "register", "buy", "purchase", "subscribe", "start", "try pro", "want pro", "want to try", "get started"]

    if any(word in text for word in greeting_words):
        return "greeting"

    if any(word in text for word in high_intent_words):
        return "high_intent"

    if any(word in text for word in pricing_words):
        return "pricing"

    return "other"


def answer_with_context(user_input: str) -> str:
    text = user_input.lower()

    if "basic" in text:
        basic = kb["pricing"]["basic"]
        return (
            f"Basic Plan costs {basic['price']} and includes "
            f"{', '.join(basic['features'])}."
        )

    if "pro" in text:
        pro = kb["pricing"]["pro"]
        return (
            f"Pro Plan costs {pro['price']} and includes "
            f"{', '.join(pro['features'])}."
        )

    if "refund" in text:
        return kb["policies"]["refund"]

    if "support" in text:
        return kb["policies"]["support"]

    if any(word in text for word in ["price", "pricing", "plan", "plans", "cost", "feature", "features"]):
        basic = kb["pricing"]["basic"]
        pro = kb["pricing"]["pro"]

        return (
            f"Here are our plans:\n"
            f"- Basic Plan: {basic['price']} | Features: {', '.join(basic['features'])}\n"
            f"- Pro Plan: {pro['price']} | Features: {', '.join(pro['features'])}\n"
            f"Policy note: {kb['policies']['refund']}. "
            f"{kb['policies']['support']}."
        )

    return "I can help with pricing, plan features, refunds, support, or getting started with the Pro plan."


def is_valid_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email))


def collect_lead_details():
    if not state["name"]:
        state["name"] = input("Bot: What's your name? ").strip()

    while not state["email"]:
        email = input("Bot: What's your email? ").strip()
        if is_valid_email(email):
            state["email"] = email
        else:
            print("Bot: Please enter a valid email address.")

    if not state["platform"]:
        state["platform"] = input("Bot: Which creator platform do you use? (YouTube/Instagram/etc.) ").strip()


def chat():
    print("Bot: Hi! I can help you with AutoStream pricing, features, and sign-up.")
    print("Bot: Type 'exit' anytime to stop.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break

        intent = detect_intent(user_input)
        state["intent"] = intent

        if intent == "greeting":
            print("Bot: Hello! You can ask about pricing, features, refunds, support, or getting started.")

        elif intent == "pricing":
            print("Bot:", answer_with_context(user_input))

        elif intent == "high_intent":
            print("Bot: Awesome! It sounds like you're interested in getting started.")
            collect_lead_details()

            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )

            print("Bot: Thanks! Your details have been captured successfully. Our team will reach out soon.")

        else:
            print("Bot:", answer_with_context(user_input))


if __name__ == "__main__":
    chat()