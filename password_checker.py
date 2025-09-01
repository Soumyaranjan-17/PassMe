import re

def check_strength(password: str) -> str:
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character variety
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    # Dictionary words check (basic)
    common_words = ["password", "123456", "qwerty", "admin"]
    if any(word in password.lower() for word in common_words):
        score = 1  # Weak if contains common word

    # Return rating
    if score <= 2:
        return "❌ Weak"
    elif score <= 4:
        return "⚠️ Medium"
    else:
        return "✅ Strong"
