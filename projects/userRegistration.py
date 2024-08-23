from preProjectFunctions import validate_name, validate_email, validate_password, top_level_domains
def validate_user(name, email, password):
    user_valid = False
    if user_valid == False:
        if validate_name(name) == False:
            if len(name) <= 2:
                raise ValueError("Username should be more than 2 characters.")
            
        if validate_email(email) == False:
            if len(email) <1:
                raise ValueError("Email address should have at least a character")
            if "@" not in email:
                raise ValueError("Email address should have an @ symbol")
            if not email.endswith(tuple(top_level_domains)):
                raise ValueError("Email address should end with at least 1 top_level_domain")
            
        if validate_password(password) == False:
            if len(password) < 8:
                raise ValueError("Password should have more than 8 characters")
            capital = False
            digit = False
            for char in password:
                if char.isupper():
                    capital = True
                if char.isdigit():
                    digit = True
            if capital == False:
                raise ValueError("Password should have at least 1 capital letter")
            if digit == False:
                raise ValueError("Password should have a number between 0-9")
        else:
            user_valid = True
    return user_valid

def register_user(name, email, password):
    users_dict = {
        'name': [],
        'email': [],
        'password': []
    }
    if validate_user(name, email, password) == True:
        users_dict['name'].append(name)
        users_dict['email'].append(email)
        users_dict['password'].append(password)
    else:
        users_dict = False
    return users_dict
        

name = input("Enter Name: ")
email = input("Enter Email: ")
password = input("Password: ")
user_dict = register_user(name, email, password)
print(user_dict)