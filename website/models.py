from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Synth(models.Model):
    CATEGORY_CHOICES = (
            ('mono', 'Monosynth'),
            ('poly', 'Polysynth'),
            ('dm', 'Drum machine'),
            )
    name = models.CharField(max_length=100, primary_key=True)
    issue_year = models.IntegerField()
    category = models.CharField(max_length=5,choices=CATEGORY_CHOICES)
    pic = models.ImageField(upload_to="synth_pics")
    maker = models.CharField(max_length=100)

    def __unicode__(self):
        return self.maker + ' ' + self.name


class Review(models.Model):
    synth = models.ForeignKey(Synth)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    review_text = models.TextField()

    def __unicode__(self):
        return self.author.username + "'s "+ self.synth.maker + " " +self.synth.name +" review"


