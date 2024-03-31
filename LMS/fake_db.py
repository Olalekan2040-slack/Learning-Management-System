from faker import Faker
import hashlib

fake = Faker()

fake_users_db = {}

for _ in range(10):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    # Hash the password
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    fake_users_db[email] = {
        "username": username,
        "email": email,
        "hashed_password": hashed_password,
        "disabled": False,
    }

print(fake_users_db)
