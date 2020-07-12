from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id) 
    return render(request, 'detail.html',{'blog':blog_detail})

#new.html을 띄워주는 함수
def new(request):
    return render(request, 'new.html')

#입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    #blog.id는 int형 이기때문에 str로 강제 형변환
    return redirect('/blog/'+str(blog.id))