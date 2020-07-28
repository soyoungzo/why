from django.shortcuts import render, redirect
from django.contrib import messages
#어떤 특정 조건이 성립됐을때 메세지를 띄어주는
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Account

def signup(request):
    if request.method == 'POST':
    # POST는 정보를 보내주는 기능인데 보안이 필요한 정보들
        user_id = request.POST.get('user_id')
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')
        email = request.POST.get('email')
        nickname = request.POST.get('nickname')
    #모든 정보를 입력하였는지, 비밀번호와 비밀번호 확인이 잘맞게 이루어졌는지
        if user_id == "" or pw1 == "" or pw2 == "" or email == "" or nickname == "":
            messages.info(request, "빈칸을 채워주십시오")
            return redirect('signup')
        # == 는 같다, != 는 다르다
        if pw1 != pw2: 
            messages.info(request, '비밀번호가 틀립니다')
            return redirect('signup')
    #지금까지의 과정은 유저가 정보를 제대로 입력했으면 그걸 다 가져오는 과정
    #받은 정보는 DB에 저장

        user = User.objects.create_user(username=user_id, password=pw1)
        #username과 password장고에서 제공해주는 DB에 있는 column내용
        user.save()
        account = Account(user=user, email=email, nickname=nickname)
        #user는 외래키(참조키)
        account.save()
        return redirect('main')

    else:
        return render(request, 'signup.html')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        #login.html에서 입력한 정보랑 user DB랑 비교하는 과정
        user = auth.authenticate(request, username=user_id, password=password)
        #user 인증 결과에 따라 로그인성공 or 에러 메세지 전달

        #user정보를 확인한 경우
        if user is not None :
            auth.login(request, user)
            return redirect('main')
    
        #확인된 회원 정보가 없을 경우
        else:
            messages.info(request, "회원정보가 일치하지 않습니다.")
            return redirect ('login')
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main')
# Create your views here.
