import csv

def register_user(name, email, password):
    # Check if the user already exists
    if not user_exists(email):
        # Open the CSV file in append mode
        with open('users.csv', 'a', newline='') as users:
            # Create a CSV writer object
            csv_writer = csv.writer(users)

            # Write the user information to the CSV file
            csv_writer.writerow([name, email, password])
            
            print(f"User {name} with email {email} registered successfully.")
    else:
        print(f"User with email {email} already exists.")

def user_exists(email):
    # Open the CSV file in read mode
    with open('users.csv', 'r', newline='') as users:
        reader = csv.reader(users)

        # Skip header if it exists
        header = next(reader, None)

        # Convert the remaining rows to a list
        rows = list(reader)

    # Extract values from the third column (index 2) assuming email is in the third column
    values = [row[2] for row in rows]

    low, high = 0, len(values) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = values[mid]

        if mid_value == email:
            return True
        elif mid_value < email:
            low = mid + 1
        else:
            high = mid - 1

    return False

def main():
    print("Welcome to MoniFit. Please register your account.")
    user_name = input("Please input your name: ")
    user_email = input("Please input your email: ")
    user_password = input("Please input your password: ")
    register_user(user_name, user_email, user_password)

if __name__ == "__main__":
    main()
