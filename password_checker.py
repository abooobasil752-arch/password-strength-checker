import re
import math
import getpass

COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "admin",
    "welcome", "letmein", "abc123", "111111", "iloveyou"
]

def calculate_entropy(password):
    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"\d", password):
        charset_size += 10
    if re.search(r"[^A-Za-z0-9]", password):
        charset_size += 32

    if charset_size == 0:
        return 0

    return round(len(password) * math.log2(charset_size), 2)


def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use 12 or more characters for stronger security.")

    if len(password) >= 16:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters like @, #, $, !.")

    if re.search(r"(.)\1{2,}", password):
        score -= 1
        suggestions.append("Avoid repeated characters like aaa or 111.")

    if re.search(r"(123|234|345|456|567|678|789|abc|bcd|qwerty)", password.lower()):
        score -= 1
        suggestions.append("Avoid common sequences like 123, abc, or qwerty.")

    if password.lower() in COMMON_PASSWORDS:
        score -= 3
        suggestions.append("Avoid common passwords.")

    entropy = calculate_entropy(password)

    if entropy >= 80:
        score += 2
    elif entropy >= 60:
        score += 1
    elif entropy < 35:
        suggestions.append("Increase password complexity and length.")

    score = max(score, 0)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, score, entropy, suggestions


print("=" * 40)
print(" Password Strength Checker")
print("=" * 40)

password = getpass.getpass("Enter a password to check: ")

strength, score, entropy, suggestions = check_password_strength(password)

print("\nResult")
print("-" * 40)
print(f"Strength: {strength}")
print(f"Score: {score}/8")
print(f"Entropy: {entropy} bits")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("\nGreat! Your password looks very strong.")

print("=" * 40)
