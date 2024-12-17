from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Tip
import random
from django.core.mail import send_mail
from django.conf import settings

# Register View
otp_storage = {}


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if email == "":
            messages.error(request, 'Please Input a valid email')
            return redirect('/register/')


        # Check for existing user
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('/register/')
        
        if Profile.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
            return redirect('/register/')

        # Generate and save OTP
        otp = random.randint(1000, 9999)
        otp_storage[email] = otp

        # Send OTP to the user's email
        send_mail(
            'OTP Code from Medicine Store',
            f'Hi {first_name} {last_name}, here is your OTP: {otp}.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        # Temporarily save user data in session
        request.session['user_data'] = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'password': password,
            'email': email,
            'phone_number': phone_number,
            'address': address
        }
        return redirect('/confirm-otp/')

    return render(request, 'register.html')


def confirm_otp_view(request):
    if request.method == "POST":
        user_data = request.session.get('user_data')
        #email = request.POST.get('email')
        email = user_data.get('email')
        otp_input = request.POST.get('otp')

        # Verify OTP
        if email in otp_storage and int(otp_input) == otp_storage[email]:
            user_data = request.session.get('user_data')
            if user_data:
                
                user = User.objects.create_user(
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    username=user_data['username'],
                    email=user_data['email'],
                )
                user.set_password(user_data['password'])
                user.save()

                Profile.objects.create(
                    user=user,
                    email=user_data['email'],
                    phone_number=user_data['phone_number'],
                    address=user_data['address']
                )

                del otp_storage[email]
                del request.session['user_data']

                messages.success(request, 'Registration successful! You can now login.')
                return redirect('/login/')
        else:
            messages.error(request, 'Invalid OTP or email')
            return redirect('/confirm-otp/')

    return render(request, 'confirm_otp.html')


# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/login/')
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

def health_tips(request):
    tips = Tip.objects.all()  # Fetch all tips
    return render(request, 'health_tips.html', {'tips': tips})
