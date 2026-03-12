from django.db import models
from accounts.models import RecruiterProfile

class Job(models.Model):
    TYPE_CHOICES = [
        ('part_time', 'Part Time'),
        ('full_time', 'Full Time'),
        ('remote_job', 'Remote Job'),
    ]

    recruiter = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE)

    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='company_logo/', null=True, blank=True)

    responsibilities = models.TextField()
    education = models.TextField()
    vacancies = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    skills = models.TextField()
    opening_date = models.DateField()
    deadline = models.DateField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title