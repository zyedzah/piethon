import hashlib

def sha256_hash(input_string):
    sha256_hash_object = hashlib.sha256()
    sha256_hash_object.update(input_string.encode('utf-8'))
    hashed_value = sha256_hash_object.hexdigest()
    return hashed_value

user_input = input("Enter a string to hash using SHA-256: ")

hashed_result = sha256_hash(user_input)

print(f"Original String: {user_input}")
print(f"SHA-256 Hash: {hashed_result}")
