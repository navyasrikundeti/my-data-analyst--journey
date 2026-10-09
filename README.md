# Python OTP Generator

A beginner-friendly Python project that generates one-time password (OTP) strings.

## Features
- Generates numeric OTPs (for example, 6 digits)
- Generates alphanumeric OTPs
- Lets the user choose the OTP length
- Uses Python's `secrets` module for secure random selection

## Requirements
- Python 3
- No third-party packages required

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python otp_generator.py
   ```
4. Choose `1` for a numeric OTP or `2` for an alphanumeric OTP.
5. Enter the desired length.

## Example
```text
OTP GENERATOR
1. Numeric OTP
2. Alphanumeric OTP
Choose an option (1 or 2): 1
Enter OTP length (for example, 6): 6
Your OTP is: [a randomly generated 6-digit OTP]
```

## Learning outcomes
- Python functions
- User input and validation
- String operations
- The standard-library `secrets` and `string` modules

## Note
This is a learning project. Generating an OTP alone does not provide a full authentication system; real applications also need secure delivery, expiry, rate limiting, and verification.
