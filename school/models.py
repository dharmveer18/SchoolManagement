from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICE = (
    ('s', 'student'),
    ('t', 'teacher'),
    ('a', 'admin')
)


class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    mobile_no = models.CharField(max_length=13,null=True, blank=True)
    photo = models.ImageField(upload_to='user_images/', null=True, blank=True)
    type_of_user = models.CharField(max_length=2, choices= USER_TYPE_CHOICE , default= 'a')
    is_user_deleted = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.username


