from django.shortcuts import render, get_object_or_404, redirect
#장고에만 있는 기능, get_object_or 404 정보가 없으면 나타나게 하는 페이지(페이지낫파운드)
from .models import Blog
from django.utils import timezone
from login.models import Account

def main(request):
    blog = Blog.objects
    text = ""
    if request.user.is_authenticated:
        txt_prime = Account.objects.get(user=request.user)
        text = txt_prime.nickname + "님 안녕하세요!"
    else:
        text = "로그인해주세요"
    #now_login = Account.objects.get(user = request.user)
    #context = {'blog':blog, 'user':now_login}
    return render(request, 'main.html', {'blog':blog, 'txt':text})

def other(request):
    account = Account.objects.get(user=request.user)
    
    return render(request,'other.html', {'account':account})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def news(request):
    return render(request, 'news.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))
    #redirect는 return값을 url로 이동해서 보여줌

def delete(request):
    del_id = request.GET['blogNum']
    #GET은 정보를 보내주는(생성해주는)
    blog = Blog.objects.get(id=del_id)
    blog.delete()
    return redirect('http://127.0.0.1:8000/')

def edit(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html', {"blog":blog_detail})

def recreate(request, blog_id):
    edit_id = request.get['blogNum']
    blog = Blog.objects.get(id=edit_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.date = timezone.datetime.now()
    blog.save()
    return redirect('main')
    
        
def port(request):
    return render(request, 'portfolio.html')

def like(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    user = request.user
    account = Account.objects.get(user=user)

    check_list_blog = account.post_like.filter(id=blog_id)
    #filter 필터된 정보들만 가져오는 -> blog_id만 가져온다

    if check_list_blog.exists():
        account.post_like.remove(blog)
        blog.like_number -= 1
        blog.save()
    #좋아요 취소

    else :
        account.post_like.add(blog)
        blog.like_number += 1
        blog.save()
    #좋아요 누름

    return redirect('main')

# Create your views here.
