from django.db import models

# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=128)
    l_name = models.CharField(max_length=128)
    e_mail = models.EmailField(max_length=128, unique=True)

# class Cfirst_name(models.Model):
#
#
#     def __str__(self):
#         return self.f_name
#
# class Clast_name(models.Model):
#
#
#     def __str__(self):
#         return self.l_name
#
# class Cemail(models.Model):
#
#
#     def __str__(self):
#         return self.e_mail
