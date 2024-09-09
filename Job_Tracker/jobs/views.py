from django.shortcuts import render, redirect
from .models import Job, Application
from .forms import JobForm, ApplicationForm

# Create your views here.

def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/create_job.html', {'form': form})

def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    applications = job.applications.all()
    return render(request, 'jobs/job_detail.html', {'job': job, 'applications': applications})

def application_details(request, pk):
    application = Application.objects.get(pk=pk)
    return render(request, 'jobs/application_details.html',{'application': application})

def apply_for_job(request, pk):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = Job.objects.get(pk=pk)
            application.save()
            return redirect('job_detail', pk=pk)
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form})