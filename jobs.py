import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobs.settings')
import django
django.setup()

from app1.models import Bangalore_jobs, Bihar_jobs, Hydrabad_jobs
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
    d1 = randint(6,9)
    phone = str(d1)
    for i in range(9):
        phone += str(randint(0,9))
    return int(phone)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('python developer','project manager','technical enginner','human resource'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        bang_record = Hydrabad_jobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,address=faddress,email=femail,phonenumber=fphonenumber)


n = int(input('enter a number of records!:'))
populate(n)