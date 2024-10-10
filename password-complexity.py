import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Calculate the strength based on criteria
    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    # Provide feedback on password strength
    if score == 5:
        return "Strong password!"
    elif 3 <= score < 5:
        return "Moderate password. Consider adding more variety."
    else:
        return "Weak password. Use a mix of uppercase, lowercase, numbers, and special characters."

# Example usage
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
