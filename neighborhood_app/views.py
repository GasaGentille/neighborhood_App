from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Neighbor,Business,Profile,Event
from .forms import ProfileForm,BusinessForm,EventForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    neighbors =Neighbor.objects.all()
    profile = Profile.objects.filter(user=current_user).first()
    return render(request,'index.html',{'neighbor':neighbors,'profile':profile})
 
@login_required(login_url='/accounts/login/')
def neighborhood(request,neighborhood_id):
    
    current_user = request.user
    neighbors = Neighbor.objects.get(id=neighborhood_id)
    business = Business.objects.filter(neighborhood = neighbors.id).all()
    events = Event.objects.filter(neighborhood = neighbors.id).all()
    profile = Profile.objects.filter(id=current_user.id).first()
    
    return render(request,'hood.html',{'business':business,'neighbors':neighbors,'event':events,'neighborhood_id':neighborhood_id})
 
@login_required(login_url='/accounts/login/')
def new_business(request):

    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business_post = form.save(commit=False)
            business_post.user = current_user
            business_post.save()
            return redirect('profile')
    else:
        form = BusinessForm()
        return render(request,'nw_business.html',{"form": form})

@login_required(login_url='/accounts/login/')
def new_events(request):

    current_user = request.user
    if request.method == 'POST':

        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event_post = form.save(commit=False)
            event_post.user = current_user
            event_post.save()
            return redirect('welcome')
    else:
        form = EventForm()
        return render(request,'nw_event.html',{"form":form})
        
@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
        return render(request,'add_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def myprofile(request):
     current_user = request.user
     profile = Profile.objects.filter(user=current_user).first()
     return render(request,'prfile.html',{"profile":profile,"current_user":current_user})

def search_business(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})