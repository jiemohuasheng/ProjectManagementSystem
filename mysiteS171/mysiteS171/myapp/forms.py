from django import forms

from .models import Announcement, Requirement, Project, Issue, Member, Issue_Detail, User


from django.contrib.auth.forms import UserCreationForm

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'author', 'description']

  #  title = forms.CharField(label='Title', max_length=10000)
   # author = forms.CharField(label='Author', max_length=50)
   # description = forms.CharField(label='Description', widget=forms.Textarea)

class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = ['title', 'customer', 'project', 'description']
    #title = forms.CharField(label='Title', max_length=10000)
    #costumer = forms.CharField(label='Costumer', max_length=50)
    #description = forms.CharField(label='Description', widget=forms.Textarea)

class IssuesForm(forms.ModelForm):
    #object_name = forms.CharField(label='Object', widget=forms.Textarea)
    #description = forms.CharField(label='Description', widget=forms.Textarea)
    class Meta:
        model = Issue
        fields = ['project', 'title', 'description', 'author']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_no','name','leader','start_date','end_date','phase','description']

class IssueDetailForm(forms.ModelForm):
    class Meta:
        model = Issue_Detail
        fields = ['answer']


class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['project_no', 'first_name', 'last_name', 'email']

#
# class MemberRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']
#
#         def _init_(self, *args, **kwargs):
#             super(UserCreationForm, self)._init_(*args, **kwargs)
#
#             self.fields['username'].widget.attrs['class'] = 'form-control'
#             self.fields['first_name'].widget.attrs['class'] = 'form-control'
#             self.fields['last_name'].widget.attrs['class'] = 'form-control'
#             self.fields['email'].widgets.attrs['class'] = 'form-control'