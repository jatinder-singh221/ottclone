from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import showform
from .models import show

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

 