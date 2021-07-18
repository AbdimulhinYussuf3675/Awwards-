from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@loging_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    project = Projects.get_all_projects()
    return render (request, 'home.html', {"projects":projects})
    
