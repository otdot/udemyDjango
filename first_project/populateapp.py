import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=20):
    for info in range(N):
        fakename = fakegen.name().split()
        fakefname = fakename[0]
        fakelname = fakename[1]
        fakeemail = fakegen.email()
        user = User.objects.get_or_create(f_name=fakefname,
        l_name=fakelname,
        e_mail=fakeemail)[0]

if __name__ == "__main__":
    print("populating script")
    populate()
    print("populating complete")
