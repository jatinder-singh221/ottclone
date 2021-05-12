from django import contrib
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import showform
from django.contrib.auth.models import User
from .models import show,watch_history
from django.contrib.auth.decorators import login_required

def create_show(request):

    if request.user.is_authenticated:
        show_form_instance = showform
        form = show_form_instance(request.POST or None )

        if request.method == 'POST':
            form = showform(request.POST, request.FILES)
            if form.is_valid():
                show = form.cleaned_data.get('show_name')
                intial = form.save(commit=False)
                intial.show_authors = request.user
                intial.save()
                messages.success(request,f'show saved for {show}.')
                return redirect('show:create')
        
        context = {'htmlform':form}
        return render(request,'addshow.html',context)
    else:
        return redirect('auth:home')    

def show_show(request):

    # if request.user.is_authenticated:
        shows = show.objects.all().only('show_name','show_title','show_vedio')
        
        context = {'show':shows}
        return render(request,'show.html',context)
    # else:
    #     return redirect('auth:home') 
 
def allitems(request,catagory_name):
    all_show = show.objects.filter(show_catagory__catagorie_name__icontains = catagory_name )
    context = {'all_items':all_show}
    return render(request,'allofcatagory.html', context)


def show_item(request,pk):
    item = show.objects.get(id = pk)
    user_name = request.user
    if request.user.is_authenticated:
        watch_history_person = watch_history.objects.get(user =user_name)
        watch_history_person.waths.add(pk)
    context = {'item':item}
    return render(request,'vedio.html',context)
    
@login_required(login_url='auth:login')
def history(request):
    user = request.user
    watchs = user.history_related
    vedio = watchs.waths.all
    context = {'watch':vedio}
    return render(request,'history.html', context)

def allshow(request):
    user = User.objects.get(id = request.user.id)
    items = user.show_related.all()
    context = {'items':items}
    return render(request,'entershow.html',context)
