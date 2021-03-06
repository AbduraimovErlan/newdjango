from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIPClient = 2
CLIENT = 3
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIPClient, 'VIP-Client'),
    (CLIENT, 'CLIENT')
)
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
    (OTHER, 'OTHER')
)
SINGLE = 1
MARRIED = 2
WIDOWED = 3
MARITAL_STATUS = (
    (SINGLE, 'SINGLE'),
    (MARRIED, 'MARRIED'),
    (WIDOWED, 'WIDOWED')
)


SCHOOL = 1
COLLEGE = 2
UNIVERSITY = 3
EDUCATION = (
    (SCHOOL, 'SCHOOL'),
    (COLLEGE, 'COLLEGE'),
    (UNIVERSITY, 'UNIVERSITY')
)

class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип Пользователя', default=CLIENT)
    phone_number = models.CharField('phone_number', max_length=100)
    age = models.IntegerField()
    nation = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Гендер')
    maritalStatus = models.IntegerField(choices=MARITAL_STATUS, verbose_name='Семейное положение', null=True)
    education = models.IntegerField(choices=EDUCATION, verbose_name='Семейное положение', null=True)