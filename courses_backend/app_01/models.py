from django.db import models


# Create your models here.


class Course(models.Model):
    code = models.CharField(max_length=10,
                            blank=False,
                            help_text='课程代码',
                            error_messages={
                                'unique': "A code with that course already exists."}
                            )
    name_en = models.CharField(max_length=100, blank=True)
    url = models.URLField()
    term = models.IntegerField(null=True)
    year = models.IntegerField(null=True)

    def __str__(self):
        return self.code


class Students(models.Model):
    name = models.CharField(max_length=30,
                            blank=False,
                            help_text='昵称',
                            error_messages={
                                'unique': "A user with that username already exists."}
                            )
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=30, blank=False)
    register_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
