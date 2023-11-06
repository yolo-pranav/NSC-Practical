from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor

# Create a DES key (8 bytes)
key = get_random_bytes(8)

# Create a DES cipher object in CBC mode
iv = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_CBC, iv=iv)

# Plain text (must be a multiple of 8 bytes)
plaintext = "Hello123"

# Padding the plaintext
plaintext = pad(plaintext.encode(), 8)

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
decipher = DES.new(key, DES.MODE_CBC, iv=iv)
decrypted_text = unpad(decipher.decrypt(ciphertext), 8)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Decrypted Text: {decrypted_text.decode()}")