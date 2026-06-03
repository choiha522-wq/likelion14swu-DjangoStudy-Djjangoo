from django.shortcuts import render, redirect


def index(request):
    #로그인한 경우 피드 페이지로
    if request.user.is_authenticated :
        return redirect("/posts/feeds/")
    #안 한 경우 로그인 페이지로
    else:
        return redirect("/users/login/")