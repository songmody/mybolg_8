from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog #admin상의 블로그프젝을 홈에 띄우기위함

def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request,'home.html',{'blogs':blogs}) #home.html에서 값을 내보내는 함수

def finish(request,blog_id):
    finishs=get_object_or_404(Blog, pk=blog_id)
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
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

