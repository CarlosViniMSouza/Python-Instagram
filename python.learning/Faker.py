# before : pip install Faker

from faker import Faker
fake = Faker()

fake.color_name()
# 'MediumYellow'

fake.name()
# 'Jhonnathan Silver'

fake.address()
# '7393 Morgan Trail \n Janiceville, D.E. 32190'

fake.city()
# 'Anglo Tryubher'

fake.job()
# 'Developer Social, community'

"""
Faker is a Python package that generates fake data for you. Whether you need to 
bootstrap your database, create good-looking XML documents, fill-in your persistence 
to stress test it, or anonymize data taken from a production service, Faker is for you. 
👨‍💻🐍
"""
