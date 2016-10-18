from django.shortcuts import render, get_object_or_404
from .models import Asp, Contact
from .forms import AddJobForm

def mainlist(request):
    all_jobs = Asp.objects.all()
    context = {'all_jobs': all_jobs}
    return render(request, 'arrowjobs/mainlist.html', context)

def job_detail(request, jobasp):
    #job_asp = Asp.objects.get(design_id = jobasp)
    job_asp = get_object_or_404(Asp, design_id = jobasp)
    context = {'job_asp': job_asp}
    return render(request, 'arrowjobs/job_detail.html', context)

def job_add(request):
    if request.method == "GET":
        form = AddJobForm(request.GET or None)
        context = {'form': form }
        return render(request, 'arrowjobs/jobaddform.html', context)
    elif request.method == "POST":
        form = AddJobForm(request.POST)
        context = {'form': form }
        if form.is_valid():
            form.save()
            return render(request, 'arrowjobs/jobaddform.html', context)
        else:
            return render(request, 'arrowjobs/jobaddform.html', context)

