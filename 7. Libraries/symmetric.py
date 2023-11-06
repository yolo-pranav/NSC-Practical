from cryptography.fernet import Fernet

# Generate a symmetric key
key = Fernet.generate_key()

# Create a Fernet cipher object
cipher = Fernet(key)

# Encrypt data
data = b"Hello, symmetric encryption!"
encrypted_data = cipher.encrypt(data)

# Decrypt data
decrypted_data = cipher.decrypt(encrypted_data)

print(f"Original Data: {data.decode()}")
print(f"Encrypted Data: {encrypted_data}")
print(f"Decrypted Data: {decrypted_data.decode()}")
