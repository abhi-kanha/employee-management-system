from django.contrib import admin
from .models import UserProfile,Attendance, Leaveapplication, Interview, Assignprojects
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Attendance)
admin.site.register(Leaveapplication)
admin.site.register(Interview)
admin.site.register(Assignprojects)