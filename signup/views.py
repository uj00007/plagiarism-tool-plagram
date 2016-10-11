from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from passlib.handlers.sha2_crypt import sha256_crypt
from .models import User
from .forms import NameForm,LoginForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


x=User()


def index(request):
    # if this is a POST request we need to process the form data
    # print(x.email)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        signupform = NameForm(request.POST)
        loginform = LoginForm(request.POST)
        # check whether it's valid:
        if signupform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            hash = sha256_crypt.encrypt(signupform.cleaned_data['your_password'])
            user = User(name=signupform.cleaned_data['your_name'], username=signupform.cleaned_data['your_username'],
                        email=signupform.cleaned_data['your_email'],password=hash)
            user.save()
            #return render(request, 'signup/success.html',{'name':signupform.cleaned_data['your_name']})
            return HttpResponseRedirect(reverse('signup:success'))
        if loginform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            listusername=[]
            listemail=[]
            listpass=[]
            listname=[]
            for user in User.objects:
                listusername.append(user.username)
                listemail.append(user.email)
                listpass.append(user.password)
                listname.append(user.name)
            if loginform.cleaned_data['nameoremail'] in listusername:
                if sha256_crypt.verify(loginform.cleaned_data['passlogin'],listpass[listusername.index(loginform.cleaned_data['nameoremail'])]):

                    n=listname[listusername.index(loginform.cleaned_data['nameoremail'])]
                    request.session['name']=n
                    #return render(request, 'signup/loginsuccess.html',{'name': user.name})
                    return HttpResponseRedirect(reverse('signup:loginsuccess'))
                else:
                    '''
                    error="wrong password"
                    return render(request, 'signup/index.html', {'formsignup': signupform,'formlogin':loginform,'error':error})
                    '''
                    return HttpResponse("<script> alert('PASSWORD INCORRECT..!!'); window.location=\"\"; </script>")
            elif loginform.cleaned_data['nameoremail'] in listemail:
                if sha256_crypt.verify(loginform.cleaned_data['passlogin'],listpass[listemail.index(loginform.cleaned_data['nameoremail'])]):

                    n=listname[listemail.index(loginform.cleaned_data['nameoremail'])]
                    request.session['name']=n
                    #return render(request, 'signup/loginsuccess.html',{'name': user.name})
                    return HttpResponseRedirect(reverse('signup:loginsuccess'))
                else:
                    '''
                    error="wrong password"
                    return render(request, 'signup/index.html', {'formsignup': signupform,'formlogin':loginform,'error':error})
                    '''
                    return HttpResponse("<script> alert('PASSWORD INCORRECT..!!'); window.location=\"\"; </script>")

            else:
                '''
                error="Invalid username or email"
                return render(request, 'signup/index.html', {'formsignup': signupform,'formlogin':loginform,'error':error})
                '''
                return HttpResponse("<script> alert('invalid username or email..!!'); window.location=\"\"; </script>")


    # if a GET (or any other method) we'll create a blank form
    else:
        signupform = NameForm()
        loginform=LoginForm()

    return render(request, 'signup/index.html', {'formsignup': signupform,'formlogin':loginform})


def success(request):
    return render(request,'signup/success.html',{})


def loginsuccess(request):
    print("this is session variable"+request.session['name'])
    return render(request,'signup/loginsuccess.html',{"name":request.session['name']})
