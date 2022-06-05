from django.shortcuts import redirect, render
from django.contrib import auth

def login(request):
    # request == POST
    if request.method == "POST":
        username = request.POST["username"]
        passward = request.POST["passward"]
        user = auth.authenticate(request, username=username, passward=passward)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'bad_login.html')
    # 로그인 시키기
    else:
        return render(request, 'login.html')

    # request == GET
    # login html 띄우기
def logout(request):
    auth.logout(request)
    return redirect('home')
