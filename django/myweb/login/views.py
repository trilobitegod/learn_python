from django.shortcuts import render, redirect, HttpResponseRedirect
from . import models, forms
import hashlib, datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def hash_code(s, salt='myweb'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = 'please check your input'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(name=username)
            except:
                message= "username doesn't exist"
                return render(request, 'login/login.html', locals())

            if not user.has_confirmed:
                message = 'your email is not confirmed'
                render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['username'] = user.name
                return redirect('/index/')
            else:
                message = "password wrong"
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')

def register(request):
    if request.session.get('is_login', None):
        redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = 'xxxx'
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            if password1 != password2:
                message = 'passwords are different'
                return render(request, 'login/register.html', locals())
            else:
                same_num_user = models.User.objects.filter(name=username)
                if same_num_user:
                    message = 'username has been registered'
                    return render(request, 'login/register.html', locals())
                same_num_email = models.User.objects.filter(email=email)
                if same_num_email:
                    message = 'email has been registered'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)
                message = 'please check your email'
                return render(request, 'login/confirm.html', locals())
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())

def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = 'invalid!'
        return render(request, 'login/confirm.html', locals())
    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delets()
        message = 'Your email is out of time'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = 'Thank you for your register.'
        return render(request, 'login/login.html', locals())

def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user,)
    return code


def send_email(email, code):
    subject = "Verification Email"
    text_content = "This is an email from {}".format(settings.EMAIL_HOST_USER)
    html_content = '''<p>Welcome to visit <a href="http://{}/confirm/?code={}" target=blank>www.localhost.com</a> to valid.</p>
                    '''.format('127.0.0.1:8000', code)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
