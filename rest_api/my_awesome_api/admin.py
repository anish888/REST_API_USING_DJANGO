from django.contrib import admin

# Register your models here.
from my_awesome_api.models import Person, Species
admin.site.register(Person)
admin.site.register(Species)