from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import NewPost,BlogPost
def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id) 
    return render(request, 'detail.html',{'blog':blog_detail})

#new.html을 띄워주는 함수

def new(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = NewPost()
        return render(request,'new.html',{'form':form})

#입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    #blog.id는 int형 이기때문에 str로 강제 형변환
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request,'blogpost.html',{'form':form})