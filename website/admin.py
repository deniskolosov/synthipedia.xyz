from django.contrib import admin

# Register your models here.
from .models import Synth, Review


class SynthAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("maker","name",)}

class ReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("author", "synth",)}

admin.site.register(Synth, SynthAdmin)
admin.site.register(Review, ReviewAdmin)
