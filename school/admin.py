from django.contrib import admin

# Register your models here.
from school.common_models import ClassName
from school.models import CustomUser

admin.site.register(CustomUser)
admin.site.register(ClassName)

