from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from .forms import custom_auth_form, custom_usercreation_form
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from shows.models import catagories, show, watch_history

def login_user(request):

    if request.user.is_authenticated:
        messages.warning(request,'Your are already Sign In')
        return redirect('auth:home')

    else:
        auth_form_instance = custom_auth_form
        form = auth_form_instance(request, request.POST or None)

        if request.method == 'POST':

            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)

                if user is not None:
                    login(request,user)
                    return redirect('auth:home')

        context = {'signin': form}
        return render(request,'login.html',context)

def signup(request):

    if request.user.is_authenticated:
        messages.warning(request,'Your are already Sign In')
        return redirect('auth:home')

    else:

        user_creation_instance = custom_usercreation_form
        signupform = user_creation_instance(request.POST or None)

        if request.method == 'POST':
            if signupform.is_valid():
                username = signupform.cleaned_data.get('username')
                group = Group.objects.get(name='normal')
                person = signupform.save(commit=False)
                person.save()
                person.groups.add(group)
                messages.success(request, f'Create account for {username}')
                return redirect('auth:login')

        context = {'singup':signupform}
        return render(request, 'signup.html',context)

def home(request):
    all_catagories = catagories.objects.all()
    shows = show.objects.filter(show_catagory__catagorie_name__icontains = 'action')
    show_movies = show.objects.filter(show_catagory__catagorie_name__icontains ='movies')
    origianls = show.objects.filter(show_catagory__catagorie_name__icontains = 'originals')
    context = {'catagories':all_catagories, 'show_item':shows, 'romance':show_movies, 'originals':origianls}

    if request.user.is_authenticated:
        user = request.user
        watchs = user.history_related
        vedio = watchs.waths.all()
        context['history'] = vedio
    return render(request,'card.html', context)

