from django.contrib import admin
from .models import CustomUser, JobSeekerProfile, RecruiterProfile


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(JobSeekerProfile)
admin.site.register(RecruiterProfile)