from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify

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
    slug = models.SlugField(max_length=40, null=True, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('synth', (), {'slug': self.slug})

    def save(self):
        super(Synth, self).save()
        self.slug = '%s/%s/%s/%s' % (
                slugify(self.maker),
                slugify(self.category),
                slugify(self.issue_year),
                slugify(self.name),
                )
        super(Synth, self).save()

    def __unicode__(self):
        return self.maker + ' ' + self.name


class Review(models.Model):
    synth = models.ForeignKey(Synth)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    review_text = models.TextField()
    slug = models.SlugField(max_length=40, blank=True,null=True)

    def save(self):
        super(Review, self).save()
        self.slug = '%s-%s-%s' % (
                slugify(self.author.username),
                slugify(self.synth.maker),
                slugify(self.synth.name),
                )
        super(Review, self).save()

    def __unicode__(self):
        return self.author.username + "'s "+ self.synth.maker + " " +self.synth.name +" review"


