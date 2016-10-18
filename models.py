from django.db import models
from django.core.urlresolvers import reverse


class Asp(models.Model):
    design_id = models.CharField(max_length=20)
    contact = models.ManyToManyField('Contact', blank=True)
    description = models.CharField(max_length=200)
    date_in = models.DateTimeField(auto_now=False, auto_now_add=True)
    asp_design = models.FileField(null=True, blank=True)

    def get_design(self):
        try:
            return self.asp_design.url
        except:
            return None

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("arrowjobs:job_detail", kwargs={"jobasp": self.design_id})


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, default="333222111")
    email = models.EmailField(max_length=200, default="__@__.__")

    def __str__(self):
        return self.name
