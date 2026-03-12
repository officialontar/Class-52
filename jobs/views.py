from django.shortcuts import redirect, render
from .models import Job

from django.contrib import messages

# Create your views here.

def create_new_jobs(request):

    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        responsibilities = request.POST.get('responsibilities')
        education = request.POST.get('education')
        vacancies = request.POST.get('vacancies')
        salary = request.POST.get('salary')
        job_type = request.POST.get('job_type')
        description = request.POST.get('description')
        skills = request.POST.get('skills')
        opening_date = request.POST.get('opening_date')
        deadline = request.POST.get('deadline')
        location = request.POST.get('location')

        # Create a new Job instance and save it to the database
        Job.objects.create(
            job_title=job_title,
            company_name=company_name,
            responsibilities=responsibilities,
            education=education,
            vacancies=vacancies,
            salary=salary,
            job_type=job_type,
            description=description,
            skills=skills,
            opening_date=opening_date,
            deadline=deadline,
            location=location
        )

        messages.success(request, 'Job created successfully!')
        return redirect ('profile')


    return render(request, 'jobs/create_new_jobs.html')