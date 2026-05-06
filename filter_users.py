import json
import re


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if
                      user["name"].lower() == name.lower()]

    if not filtered_users:
        print("No users found with that name.")
    for user in filtered_users:
        print(user)


def filter_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    if not filtered_users:
        print("No users found with that age.")
    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    if not filtered_users:
        print("No users found with that email.")
    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    while True:
        filter_option = input(
            "\nWhat would you like to filter by? (Currently, only 'name', 'age' "
            "and 'email' is supported): "
        ).strip().lower()

        if filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").strip()
            if not name_to_search:
                print("Error: Name cannot be empty.")
            else:
                filter_users_by_name(name_to_search)

        elif filter_option == "age":
            age_input = input("Enter an age to filter users: ").strip()
            try:
                age_to_search = int(age_input)
                if age_to_search < 0:
                    print("Error: Age cannot be negative.")
                else:
                    filter_by_age(age_to_search)
            except ValueError:
                print(f"Error: '{age_input}' is not a valid age. Please enter a whole number.")

        elif filter_option == "email":
            print("Reminder: Email must be in the format 'example@example.com'")
            email_to_search = input("Enter an email to filter users: ").strip()
            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email_to_search):
                print(f"Error: '{email_to_search}' does not look like a valid "
                      f"email address.")
            else:
                filter_users_by_email(email_to_search)

        else:
            print("Filtering by that option is not yet supported.")

        again = input("\nWould you like to filter by another option? "
                      "(yes(y)/no(n)): ").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break
