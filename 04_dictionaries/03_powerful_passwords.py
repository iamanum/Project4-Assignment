from hashlib import sha256

def hash_password(password):
    """Hash the password using SHA-256"""
    return sha256(password.encode()).hexdigest()

def verify_credentials(username, password, stored_data):
    """Verify if the username exists and the password matches the stored hash."""
    if username in stored_data:
        if hash_password(password) == stored_data[username]:
            return True
        else:
            return False
    return False

def main():
    stored_data = {
        'anum': 'bbhhkk29366f4d6b1385fc561ff3ee1a791612b579ecd8685ddce907ce8a0c9c',
        'example': 'eca1dbf5hihoy8y9uv2d4d7f331c2a01a48eecc0e555b63f2aad9061a929'
    }
    
    attempts = 3  # Allow up to 3 login attempts
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if verify_credentials(username, password, stored_data):
            print("Login successful!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid credentials. You have {attempts} attempt(s) left.")
            else:
                print("Too many failed attempts. Access denied.")

if __name__ == "__main__":
    main()
