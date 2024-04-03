from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Occupation(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='main/about', null=True, blank=True)
    date = models.DateField()
    address = models.TextField(max_length=300)
    zip_code = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(blank=True, help_text='Please enter your phone number')
    project_complete = models.IntegerField(default=0)
    cvv = models.FileField(upload_to='main/cvv')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Partner(models.Model):
    image = models.ImageField(upload_to='main/partner', null=True)
    link = models.URLField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Education(models.Model):
    years = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Experience(models.Model):
    years = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Award(models.Model):
    years = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Skills(models.Model):
    title = models.CharField(max_length=25)
    percentage = models.IntegerField()
    Last_week = models.IntegerField()
    Last_month = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='main/services')
    link = models.URLField(null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=255)
    category = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='main/project')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Done(models.Model):
    title = models.CharField(max_length=25)
    number = models.IntegerField(default=0)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class MeContact(models.Model):
    address = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='main/contact')
    number = PhoneNumberField(null=True, help_text='Please enter your phone number')
    li_me = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, help_text='Please enter your email address')
    web_site = models.CharField(max_length=25)
    website = models.URLField(null=True, blank=True)


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

