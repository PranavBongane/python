def validate_email(email):
    if len(email) >= 6:
        if email[0].isalpha():
            if("@" in email) and (email.count("@") == 1):
                at_index = email.index("@")
                dot_index = email.rfind(".")
                if dot_index > at_index:
                        if " " not in email:
                            for char in email:
                                if char.isalnum():
                                    continue
                                elif char in ["_", "@", "."]:
                                    continue
                            else:
                                return "Invalid e-mail (special characters not allowed 🦩)"
                            return "Valid Email....🥳"                    
                        else:
                            return("Invalid e-mail (e-mail can not contein empty spaces...🦩)")
                else:
                    return("Invalid e-mail ('.' character not present...🦩)")
            else:
                return("Invalid e-mail ('@' char error)...🦩")
        else:
            return("Invalid e-mail (starting character must be an alphabet)...🦩")
    else:
        return("Invalid e-mail (character length dosenot match)...🦩")


def main():
    email = input("Enter e-mail to be validated: ").lower()
    print(validate_email(email))

if __name__ == "__main__":
    main()