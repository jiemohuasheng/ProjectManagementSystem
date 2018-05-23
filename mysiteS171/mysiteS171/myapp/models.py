from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    description = models.CharField(max_length=100000)
    date = models.DateField()
    def __str__(self):
        return self.title

class Member(models.Model):
    #members_no = models.IntegerField(max_length=5,primary_key=True)
    project_no = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.first_name + self.last_name

class Project(models.Model):
    project_no = models.IntegerField(primary_key=True)
    members = models.ManyToManyField(Member,blank=True)
    name = models.CharField(max_length=50)
    leader = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    Communication = 0
    Planning = 1
    Modeling = 2
    Construction = 3
    Deployment = 4
    phase_choice = (
        (0, 'Communication'),
        (1, 'Planning'),
        (2, 'Modeling'),
        (3, 'Construction'),
        (4, 'Deploylment')
    )
    phase = models.IntegerField(default=0, choices=phase_choice)
    description = models.CharField(max_length=100000)

    def __str__(self):
        return str(self.project_no)+'  '+ self.name

class Requirement(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    date = models.DateField()
    def __str__(self):
        return self.title

class Issue(models.Model):

    project = models.ForeignKey(Project)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=100000)
    author = models.ForeignKey(User)
    date =  models.DateField()

    def __str__(self):
        return self.title


class Issue_Detail(models.Model):
    answer = models.CharField(max_length=100000)
    replyer = models.ForeignKey(User)
    issue = models.ForeignKey(Issue)