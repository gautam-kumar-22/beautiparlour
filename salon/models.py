"""Create your models here."""
from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

GENDER_CHOICES =( 
    ("female", "female"),
    ("male", "male"),
)

CONTENT_CHOICES =( 
    ("about", "about"),
    ("service", "service"),
    ("contact", "contact"),
    ("footer", "footer"),
)

class TimeStampedModel(models.Model):
    """TimeStampedModel.
    An abstract base class model that provides self-managed "created" and
    "updated" fields.
    """

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        get_latest_by = 'modified_on'
        ordering = ('-modified_on', '-created_on',)
        abstract = True


class Slider(TimeStampedModel):
    """Slider model."""

    topic = models.CharField(max_length=50, null=True, blank=True)
    sub_topic = models.CharField(max_length=50, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Slider"


class Service(TimeStampedModel):
    """Service model."""

    topic = models.CharField(max_length=50, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Service"


class Category(TimeStampedModel):
    """Category model."""

    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class Gallery(TimeStampedModel):
    """Gallery model."""

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Gallery"


class CompanyInfo(TimeStampedModel):
    """CompanyInfo model."""

    address = models.CharField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    fb = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    google = models.URLField(max_length=200, null=True, blank=True)
    pinterest = models.URLField(max_length=200, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)
    timing = models.CharField(max_length=254, null=True, blank=True)
    company_name = models.CharField(max_length=254, null=True, blank=True)
    logo = models.FileField(null=True, blank=True)
    slogan = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.company_name or '-'

    class Meta:
        verbose_name_plural = "CompanyInfo"


class AboutUs(TimeStampedModel):
    """AboutUs model."""

    topic = models.CharField(max_length=255, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)
    discription2 = RichTextUploadingField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.discription

    class Meta:
        verbose_name_plural = "AboutUs"


class Passion(TimeStampedModel):
    """Passion model."""

    topic = models.CharField(max_length=255, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Passion"


class ContactUs(TimeStampedModel):
    """ContactUs model."""

    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True) 
    website = models.URLField(max_length=200, null=True, blank=True)
    message = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ContactUs"

class Content(TimeStampedModel):
    """Content model."""

    name = models.CharField(choices=CONTENT_CHOICES, max_length=200, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Content"


class Facilities(TimeStampedModel):
    """ParlorFacilities model."""

    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Facilities"
