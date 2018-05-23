# Register your models here.
from django.contrib import admin

from .models import Announcement, Requirement, User, Project, Issue, Member, Issue_Detail

# Register your models here.



admin.site.register(Announcement)
admin.site.register(Requirement)

admin.site.register(Issue_Detail)
#admin.site.register(Project)
admin.site.register(Member)

#class MemberAdmin(admin.ModelAdmin):
#    list_display = ['first_name','last_name','get_courses']
#    def joined_projects(self,obj):
#        joined_projects = list(Member.objects.get(first_name=obj.firstname).course_set.all())
#        return joined_projects
#admin.site.register(Member,MemberAdmin)

admin.site.register(Issue)
#admin.site.register(Project)

class ProjectAdmin (admin.ModelAdmin):
    filter_horizontal = ('members',)
admin.site.register(Project, ProjectAdmin)

#class IssueAdmin (admin.ModelAdmin):
   # filter_horizontal = ('project_no',)
#    list_display = ['object','announcer','description','time']
#admin.site.register(Issue, IssueAdmin)

# class CourseAdmin (admin.ModelAdmin):
#     filter_horizontal = ('students',)
#
#
# class BookAdmin(admin.ModelAdmin):
#   list_display=['title','author','numpages','in_stock']

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['first_name','last_name','get_courses']
    # def register_courses(self,obj):
    #     register_courses = list(Student.objects.get(first_name=obj.firstname).course_set.all())
    #     return register_courses
# admin.site.register(Student,StudentAdmin)
