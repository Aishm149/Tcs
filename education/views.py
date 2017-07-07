from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
#from .models import Profile
#from .forms import ProfileForm
from .models import Education
from .forms import CompanyForm

from .forms import SecondaryEducationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import SignUpForm
from django.utils import timezone
from django.shortcuts import render
from .models import Education
from django.db.models import Q
from .forms import SearchForm
from itertools import chain


def results(request):
    form = SearchForm()
    query = request.GET.get("search")
    q_list = Education.objects.all().values('name', 'work', 'skills').order_by('name')
    if query:
        q_list = q_list.filter(Q(work = query)).order_by('name')
    return render (request, 'education/results.html', {'query': query ,'q_list':q_list,  'form' : form })


@login_required
def home(request):
    #name = request.user.username
    return HttpResponseRedirect(reverse(edu_new, args=[request.user.username]))
   # return redirect('education/' + name + '/')

# def profile(request):
#     name = request.user.username
#    # return HttpResponseRedirect(reverse(edu_new, args=[request.user.username]))
#     return redirect('education/' + name + '/')


def profile(request, name):
    user = get_object_or_404(User, username=name)
    return render(request, 'education/edu_edit.html', {'profile': user})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def edu_new(request):
    if request.method == "POST":
        form = SecondaryEducationForm(request.POST)
        if form.is_valid():
            Education = form.save(commit=False)
            Education.userID = request.user
            Education.created_date = timezone.now()
            Education.save()
    else:
        form= SecondaryEducationForm()
    return render(request, 'education/edu_edit.html', {'form': form, })


def company_new(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            Education = form.save(commit=False)
            # Education.userID = request.user
            Education.created_date = timezone.now()
            Education.save()
    else:
        form = CompanyForm()
    return render(request, 'education/edu_edit2.html', {'form': form, })





            # def personal_details(request):
#     if request.method == "POST":
#         form = PersonalDetails(request.POST)
#         if form.is_valid():
#             Education = form.save(commit=False)
#             Education.userID = request.user
#             Education.created_date = timezone.now()
#             Education.save()
#     else:
#         form= PersonalDetails()
#
#     if request.method == "POST":
#         formset = Links(request.POST)
#         if formset.is_valid():
#             Education = formset.save(commit=False)
#             Education.userID = request.user
#             Education.created_date = timezone.now()
#             Education.save()
#     else:
#         formset = Links()
#
#     return render(request, 'education/personal_edit.html', {'form': form,
#                                                             'formset': formset})
#
#
# def internship_details(request):
#     if request.method == "POST":
#         form = InternshipDetails(request.POST)
#         if form.is_valid():
#             Education = form.save(commit=False)
#             Education.userID = request.user
#             Education.created_date = timezone.now()
#             Education.save()
#     else:
#         form= InternshipDetails()
#
#     return render(request, 'education/internship.html', {'form': form})