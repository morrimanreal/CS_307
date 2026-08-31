from models import Register, User, Profile, LoginInformation


def main():
    # Register a new user
    registration = Register(
        registrationId=1,
        email="student@example.com",
        phoneNumber=5551234567,
        userName="student1",
        password="Password123"
    )

    print(registration.create())

    # Create a user object to manage the registration
    user = User(userId=1001)
    user.add(registration)

    print(f"User {user.userId} registrations: {len(user.registrations)}")

    # Create a profile object
    profile = Profile(
        profileId=501,
        date="2026-08-31",
        activity="Account created",
        description="Initial user profile"
    )

    print("\n" + profile.show())

    # Create a login information object
    login = LoginInformation(
        loginId=7001,
        userName="student1",
        password="Password123",
        accountNumber=1001
    )

    login.attach_profile(profile)

    print("\n" + login.create())

    # Validate login
    entered_user_name = "student1"
    entered_password = "Password123"

    if login.validate(entered_user_name, entered_password):
        print("Login successful.")
    else:
        print("Invalid username or password.")

    # Update login information
    login.update(userName="student_updated")

    print(f"Updated username: {login.userName}")

    # Delete the registration from the user object
    removed = user.delete(registration.registrationId)  # Delete the registration from the user object
    print(f"Registration deleted: {removed}")


if __name__ == "__main__":
    main()
