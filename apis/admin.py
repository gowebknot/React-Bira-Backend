from django.contrib import admin

# Register your models here.
from apis.models import *

admin.site.register([UserProfile, Issue])
