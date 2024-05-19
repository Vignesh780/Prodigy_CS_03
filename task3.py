import re

def assess_password_strength(password):
    # Define regex patterns for different character types
    upper_case = re.compile(r'[A-Z]')
    lower_case = re.compile(r'[a-z]')
    numbers = re.compile(r'[0-9]')
    special_chars = re.compile(r'[^a-zA-Z0-9]')

    # Assess password length
    length_score = min(10, len(password) * 2)

    # Assess presence of character types
    upper_case_score = 2 if upper_case.search(password) else 0
    lower_case_score = 2 if lower_case.search(password) else 0
    numbers_score = 2 if numbers.search(password) else 0
    special_chars_score = 3 if special_chars.search(password) else 0

    # Calculate total score
    total_score = length_score + upper_case_score + lower_case_score + numbers_score + special_chars_score

    # Assess password uniqueness and commonality (not implemented in this basic version)

    return total_score

def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)
    
    if strength >= 15:
        print("Password is Strong")
    elif strength >= 10:
        print("Password is Medium")
    else:
        print("Password is Weak")

if __name__ == "__main__":
    main()
