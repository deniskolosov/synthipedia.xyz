from django.contrib import admin

# Register your models here.
from .models import Synth, Review

admin.site.register(Synth)
admin.site.register(Review)
