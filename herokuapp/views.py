from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Heroku #admin상의 블로그프젝을 홈에 띄우기위함

def home(request):
    herokus = Heroku.objects #쿼리셋
    return render(request,'home.html',{'herokus':herokus}) #home.html에서 값을 내보내는 함수

def finish(request,heroku):
    finishs=get_object_or_404(heroku, pk=heroku)
    return render(request,'finish.html',{'finishs':finishs})
    
def drink(request):
    return render(request,'drink.html')

def food(request):
    return render(request,'food.html')

def fashion(request):
    return render(request,'fashion.html')

def specialprice(request):
    return render(request,'specialprice.html')
    
def message(request):
    return render(request,'message.html')

def create(request): #입력받은 내용을 데베에 넣어주는 함수
    heroku=Heroku()
    heroku.title=request.GET['title']
    heroku.body=request.GET['body']
    heroku.pub_date=timezone.datetime.now()
    heroku.save()
    return redirect('/heroku/'+str(heroku.id))

