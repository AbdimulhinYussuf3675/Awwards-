from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Projects
from django.contrib.auth.models import User
from . forms import UpdateUser,UpdateProfile, ProjectsForm
from django.contrib import messages
from django.db.models import Q
from django.views.generic import CreateView

# Create your views here.


@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    projects = Projects.get_all_projects()
    return render (request, 'home.html', {"projects":projects})

@login_required
def profile(request):
  current_user = request.user
  projects = Projects.objects.filter(user_id = current_user.id).all
  return render(request,'profile.html',{"projects":projects})   

@login_required
def update_profile(request):
  if request.method == 'POST':
    u_form = UpdateUser(request.POST,instance=request.user)
    p_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    u_form = UpdateUser(instance=request.user)
    p_form = UpdateProfile(instance=request.user.profile) 
    
  params = {
    'u_form':u_form,
    'p_form':p_form
  }
  return render(request,'update_profile.html', params)

@login_required(login_url='/accounts/login/')
def search(request):
   if 'title' in request.GET and request.GET['title']:
       search_term = request.GET.get('title')
       print(search_term)
       searched_projects = Projects.search_by_title(search_term)
       message = f"{search_term}"
       print(message)
       print(searched_projects)
       return render(request, "search.html", {"message": message, "searched_projects": searched_projects})
   else:
       message = "You haven't searched for any Pics"
       return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def submission(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
            return redirect('/')
    else:
        form = ProjectsForm()
    return render(request, 'submit.html', {"form": form})
    
class ProjectCreatView(CreateView):
    model = Projects
    fields = ['title','image' ,'project_description','site','country']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
