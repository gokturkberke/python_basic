#terminalde pip install faker komuduyla indirdik ilk once
from faker import Faker

fake = Faker()

print(fake.email())
print(fake.country())
print(fake.name())
print(fake.text())
print(fake.url())