import re
def validate_email(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9._+]*@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$'
    # if re.match(pattern, email):
    if re.fullmatch(pattern,email):
        return "Valid e-mail ✅"
    else:
        return "Invalid e-mail ❌"


def main():
    email = input("Enter e-mail to be validated: ").lower()
    print(validate_email(email))

if __name__ == "__main__":
    main()