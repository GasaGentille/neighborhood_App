from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.shortcuts import render,redirect
from .models import Project,Profile, Review
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,ProfileForm,ReviewForm


# Create your views here.

# @login_required(login_url='/accounts/login/')
# def project(request):
#     projects = Project.objects.all()
#     return  render (request,'index.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def profile(request, username=None):
    current_user = request.user
    prjects = Project.objects.filter(user = current_user)
    return  render (request,'profile.html',locals(),{"prjects":prjects})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('/')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    prof_update = Profile.objects.filter(user=current_user).first()
    projects = Profile.objects.filter(user=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
    
        if form.is_valid():
            project=form.save(commit=False)
            project.user=current_user
            project.save()
            
            return redirect('profile')
        
    else:
        
        form = ProfileForm()
    return render(request, 'add_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    prof_update = Profile.objects.filter(user=current_user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
    
        if form.is_valid():
            profile=form.save(commit=False)
            Profile.objects.filter(id = prof_update.id).update(profile_photo =profile.profile_photo,bio=profile.bio)
            
            return redirect('profile')
        
    else:
        
        form = ProfileForm()
    return render(request, 'update.html', {"form": form})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
