from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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
            user = User(name=signupform.cleaned_data['your_name'], username=signupform.cleaned_data['your_username'],
                        email=signupform.cleaned_data['your_email'],password=signupform.cleaned_data['your_password'])
            user.save()
            #return render(request, 'signup/success.html',{'name':signupform.cleaned_data['your_name']})
            return HttpResponseRedirect(reverse('signup:success'))
        if loginform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            for user in User.objects:
                if user.username==loginform.cleaned_data['nameoremail'] or user.email==loginform.cleaned_data['nameoremail']:
                    if user.password==loginform.cleaned_data['passlogin']:
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
    return render(request,'signup/loginsuccess.html',{})
