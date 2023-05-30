from django.shortcuts import render
from .models import music_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.



def home(request):
    
    data = music_model.objects.all()
    paginator = Paginator(data, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data1 = music_model.objects.all()
    return render(request, 'home.html', {'data': page_obj,'data1': data1})
   
def playondemand(request,id):
    data = music_model.objects.get(id=id)
    data1 = music_model.objects.all()

    return render(request,'home.html',{'ondemand':data,'data1': data1})