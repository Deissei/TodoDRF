from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser


class TodoUser(AbstractUser):
    def get_age_user(self, year):
        yy, mm, dd = str(date.today()).split('-')
        yyy = int(yy) - int(year)
        return yyy


    date_of_birth = models.DateField(blank=True, null=True)

    @property
    def age_user(self):
        return self.get_age_user(self.date_of_birth.year)
