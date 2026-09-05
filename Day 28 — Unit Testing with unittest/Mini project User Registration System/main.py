# Main File for testing

def validate_username(username):
    return len(username) >= 5


def validate_age(age):
    return age >= 18


def create_user(username, age):
    if not validate_username(username):
        raise ValueError("Username too short")

    if not validate_age(age):
        raise ValueError("User must be 18+")

    return {
        "username": username,
        "age": age
    }
if __name__ =="__main__":
    username=input("Ente user_name :")
    age=int(input("Enter user age :"))
    result=create_user(username,age)
    print(result)