"""Simple numeric and alphanumeric OTP generator."""
import secrets
import string


def generate_numeric_otp(length=6):
    """Return a numeric OTP with the requested number of digits."""
    if length < 1:
        raise ValueError("OTP length must be at least 1.")
    return "".join(secrets.choice(string.digits) for _ in range(length))


def generate_alphanumeric_otp(length=6):
    """Return an alphanumeric OTP with the requested number of characters."""
    if length < 1:
        raise ValueError("OTP length must be at least 1.")
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


def main():
    print("OTP GENERATOR")
    print("1. Numeric OTP")
    print("2. Alphanumeric OTP")
    choice = input("Choose an option (1 or 2): ").strip()

    raw_length = input("Enter OTP length (for example, 6): ").strip()
    try:
        length = int(raw_length)
        if length < 1:
            raise ValueError
    except ValueError:
        print("Please enter a whole number greater than zero.")
        return

    if choice == "1":
        otp = generate_numeric_otp(length)
    elif choice == "2":
        otp = generate_alphanumeric_otp(length)
    else:
        print("Invalid option. Please choose 1 or 2.")
        return

    print(f"Your OTP is: {otp}")
    print("Demo project only: do not use this as a complete authentication system.")


if __name__ == "__main__":
    main()
