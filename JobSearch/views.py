from django.http import HttpResponse
from django.shortcuts import render
from JobSearch.forms import SearchForm
from django.template import loader
import JobSearch.jobsearcher

# Create your views here.
def index(request):
    form = SearchForm()
    return render(request, 'index.html',{'form':form})

def results(request):
    if request.method == "POST":
        newForm = SearchForm(request.POST)
        if newForm.is_valid():
            job_title = newForm.cleaned_data['job_title']
            location = newForm.cleaned_data['location']

            jobs = JobSearch.jobsearcher.main(job_title,location)
            context = {'jobs':jobs,}
            template = loader.get_template('results.html')
            return HttpResponse(template.render(context,request))
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form':form})
