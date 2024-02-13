from faker import Faker

fake = Faker()

# Generate 1020 random legitimate names
random_names = [fake.first_name() + ' ' + fake.last_name() for _ in range(1020)]

# Save the names to a file
with open('names.txt', 'w') as file:
    for name in random_names:
        file.write(name + '\n')

print("Legitimate names saved to names.txt")

