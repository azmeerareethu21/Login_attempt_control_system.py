import time

# Correct password
correct_password = "Admin@123"

# Settings
max_attempts = 3
attempts = 0
lock_time = 10   # seconds

print("=== Login Attempt Control System ===")

while attempts < max_attempts:

    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful! Access Granted.")
        break

    else:
        attempts += 1
        remaining = max_attempts - attempts

        print("Incorrect password!")

        if remaining > 0:
            print("Attempts left:", remaining)

        else:
            print("\nToo many failed attempts!")
            print("Account locked temporarily.")

            time.sleep(lock_time)

            print("\nAccount unlocked. Try again.")
            attempts = 0

