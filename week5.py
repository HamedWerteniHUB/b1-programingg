# imports
import string
import random   # for the random message at the end

# --- Part A: simple validation functions ---

def check_min_length(password, min_len = 8):
    # check if password has enough letters
    if len(password) >= min_len:
        return True
    else:
        return False


def has_uppercase(password):
    # check for uppercase letters
    for ch in password:
        if ch in string.ascii_uppercase:
            return True
    return False    # maybe forgot one uppercase


def has_lowercase(password):
    # checks small letters
    for x in password:
        if x.islower():    # using islower here, it's easier
            return True
    return False


def has_digit(password):
    # check numbers
    for number in password:
        if number.isdigit():
            return True
    return False


def has_special_char(password):
    # check special characters like !@#$
    special = string.punctuation  # all special signs
    for s in password:
        if s in special:
            return True
    return False



# --- part B: master validation ---

def validate_password(password):

    results = {}

    # calling the functions
    results["min_length"] = check_min_length(password)
    results["uppercase"] = has_uppercase(password)
    results["lowercase"] = has_lowercase(password)
    results["digit"] = has_digit(password)
    results["special"] = has_special_char(password)

    # maybe not the cleanest but works
    if (results["min_length"] and results["uppercase"]
        and results["lowercase"] and results["digit"]
        and results["special"]):
        results["is_valid"] = True
    else:
        results["is_valid"] = False

    return results



# --- Part C: user interface ---

print("=== Password Checker ===")
user_pass = input("Enter password to test: ")

check = validate_password(user_pass)

print("\n--- Validation Results ---")

# printing results one by one
print("Minimum length (8):", "Met" if check["min_length"] else "Not met")
print("Has uppercase:", "Met" if check["uppercase"] else "Not met")
print("Has lowercase:", "Met" if check["lowercase"] else "Not met")
print("Has digit:", "Met" if check["digit"] else "Not met")
print("Has special char:", "Met" if check["special"] else "Not met")

print("\nOverall password strength:")

if check["is_valid"]:
    print("✔ Strong password!")
else:
    print("✘ Weak password!")

    # random encouragement
    messages = [
        "Try adding more symbols!",
        "Maybe put some numbers?",
        "Use at least one BIG letter!",
        "You can do better, keep trying!",
        "Short passwords are easy to guess!"
    ]

    # a random hint
    print("Hint:", random.choice(messages))
