from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm


# Create your views here.

def login_view(request) :
    #사용자가 이미 로그한 경우
    if request.user.is_authenticated :
        return redirect('/posts/feeds')

    if request.method == "POST" :
        # LoginForm 인스턴스 생성 + 입력 데이터는 request.POST
        form = LoginForm(data = request.POST)

        # 유효성 검사
        if form.is_valid() :
            username = form.clenaed_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username = username, password = password)

            if user:
                login(request, user)
                return redirect('/posts/feeds')
            else:
                form.add_error(None, "Username or password is incorrect")

        context = {"form" : form}
        return render(request, "users/login.html", context)
    else:
        form = LoginForm()
        context = {"form" : form}
        return render(request, "users/login.html", context)


def logout_view(request) :
    logout(request)

    return redirect('/users/login')

def signup(request) :
    form = SignupForm()
    context = {"form" : form}
    return render(request, "users/signup.html")
