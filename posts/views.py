from django.shortcuts import render, redirect


# Create your views here.

def feeds(request) :
    #요청한 사용자가 AnonymousUser
    if not request.user.is_authenticated :
        #로그인 페이지로 이동시킴
        return redirect('/users/login/')
    return render(request, 'posts/feeds.html')