from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, UserExtraInfoForm
from myblog.models import UserExtraInfo


def signup_login(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        user_extra_form = UserExtraInfoForm(request.POST, request.FILES)
        login_form = AuthenticationForm(request=request, data=request.POST)
        if signup_form.is_valid() and user_extra_form.is_valid():
            user = signup_form.save()
            user_extra = user_extra_form.save(commit=False)
            user_extra.user = user
            user_extra_form.save()
            username = signup_form.cleaned_data.get('username')
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('myblog:home')
        elif login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data.get('username'),
                                password=login_form.cleaned_data.get('password'))
            login(request, user)
            return redirect('myblog:home')
        else:
            return render(request, 'registration/login.html', {'signup_form': signup_form, 'login_form': login_form,
                                                               'user_extra_form': user_extra_form})
    else:
        signup_form = SignUpForm()
        user_extra_form = UserExtraInfoForm()
        login_form = AuthenticationForm()
    return render(request, 'registration/login.html', {'signup_form': signup_form, 'login_form': login_form,
                                                       'user_extra_form': user_extra_form})
