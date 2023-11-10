from werkzeug.security import generate_password_hash, check_password_hash

hash = generate_password_hash('roottoor')
print(hash)
hash_check = check_password_hash(hash, "roottoor")
print(hash_check)