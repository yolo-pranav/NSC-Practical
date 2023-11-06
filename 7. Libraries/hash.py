import hashlib

data = b"Hello, hashing values!"

# Calculate the MD5 hash
md5_hash = hashlib.md5(data).hexdigest()

# Calculate the SHA-256 hash
sha256_hash = hashlib.sha256(data).hexdigest()

print(f"Data: {data.decode()}")
print(f"MD5 Hash: {md5_hash}")
print(f"SHA-256 Hash: {sha256_hash}")
