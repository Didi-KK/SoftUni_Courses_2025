def password_validator(user_password: str) -> list:
    error_messages = []
    if len(user_password) not in range(6, 10 +1):
        error_messages.append("Password must be between 6 and 10 characters")

    if not user_password.isalnum():
        error_messages.append("Password must consist only of letters and digits")

    digits_count = 0
    for current_character in user_password:
        if current_character.isdigit():
            digits_count += 1
    if digits_count < 2:
        error_messages.append("Password must have at least 2 digits")

    return error_messages

some_password = input()
validation_messages = password_validator(some_password)
if len(validation_messages) > 0:
    print("\n".join(validation_messages))
else:
    print("Password is valid")
