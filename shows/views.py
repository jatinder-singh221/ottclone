from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import showform
from django.contrib.auth.models import User
from .models import show,watch_history

def create_show(request):

    # if request.user.is_authenticated:
        show_form_instance = showform
        form = show_form_instance(request.POST or None )

        if request.method == 'POST':
            form = showform(request.POST, request.FILES)
            
            if form.is_valid():
                return HttpResponse('valid')
        
        context = {'htmlform':form}
        return render(request,'addshow.html',context)
    # else:
    #     return redirect('auth:home')    

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
    watch_history_person = watch_history.objects.get(user =user_name)
    watch_history_person.waths.add(pk)

    context = {'item':item}
    return render(request,'vedio.html',context)
    

def history(request):
    user = request.user
    watchs = user.history_related
    vedio = watchs.waths.all
    context = {'watch':vedio}
    return render(request,'history.html', context)
