from .models import Job
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class job_list(ListView):
    model = Job

    def get_context_data(self):

        pass


class detail_job(DetailView):
    model = Job

    def get(self,id):
        pass
