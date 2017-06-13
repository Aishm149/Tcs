from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.utils import timezone


#def login_list(request):
 #   profiles = Profile.objects.all()
  #  return render(request, 'LoginA/login_list.html', {'profiles': profiles})


def profile_new(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            Profile = form.save(commit=False)
            Profile.userID = request.user
            Profile.created_date = timezone.now()
            Profile.save()
    else:
        form = ProfileForm()
    return render(request, 'LoginA/profile_edit.html', {'form': form})


