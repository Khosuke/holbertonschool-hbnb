# Script to hash Administrator User password
import bcrypt

password = "admin1234".encode("utf-8")  # Convert the password to bytes
salt = bcrypt.gensalt()  # Generate a salt
hashed_password = bcrypt.hashpw(password, salt)  # Hash the password

print(hashed_password.decode())  # Print the hashed password
