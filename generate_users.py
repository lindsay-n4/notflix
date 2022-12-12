from faker import Faker

fake = Faker()

users = fake.json(
    num_rows=100,
    data_columns = [
        ('firstname', 'first_name'),
        ('lastnight', 'last_name'),
        ('username', 'user_name'),
        ('password', 'password')
    ]
)

with open('users.json', 'w') as f:
    f.write(users)
