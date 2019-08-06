from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from login.forms import LoginForm, SignupForm
from django.contrib.auth import login as auth_login, authenticate


# Create your views here.




'''@csrf_protect
def login(request):
    print("Inside login")
    if request.method == 'POST':
        print("Post request")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/show')
    csrfContext=RequestContext(request)
    login_form=LoginForm()
    return render(request,'login.html',{'form': login_form},csrfContext)'''

    
@csrf_protect
def signup(request):
    if request.method == 'POST':
        signup = SignupForm(request.POST)
        if signup.is_valid():
            print("before saving!!")
            user = signup.save()
            print("After Saving!!")
            user.set_password(user.password)
            user.save()
            username = user.username
            raw_password = signup.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('/product/show')

    csrfContext=RequestContext(request)
    signup_form=SignupForm()
    return render(request,'register.html', {'form': signup_form},csrfContext)


