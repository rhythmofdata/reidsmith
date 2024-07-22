from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from reunion import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
from django.core.mail import EmailMessage, send_mail, send_mass_mail  # Might use mass_mail later
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile
from .forms import UserProfileForm



# See reunion/info.py for email confirmation code

#home
def home(request):

    return render(request,"index.html")



#sign in
def signIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request, "index.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials!  Please enter correct username and password or register.")
            return redirect('home')

    return render(request, "signin.html")



#sign out
def signOut(request):
    logout(request)
    #messages.success(request,"Logged out successfully")
    return redirect("home")


#sign up
def signUp(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['emailaddress']
        password1 = request.POST['password']
        password2 = request.POST['confirmpass']

        if User.objects.filter(username=username):
            messages.error(request, "Sorry, that username already exists! Please try a different username.")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Sorry, that email address is  already registered! Please use a different one.")
            return redirect('home')
        
        if len(username) > 15:
            messages.error(request,"Sorry, that username is too long.  Please keep it less then 15 characters long.")
            return redirect('home')
        

        if password1 != password2:
            messages.error(request,"Password doesn't match confirmation password!")

        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric!")
            return redirect("home")

        newuser = User.objects.create_user(username, email, password1)  # Create this user
        newuser.first_name = fname
        newuser.last_name = lname
        newuser.is_active = False
        newuser.save()

        messages.success(request,"Congratulations! You are signed up! We have sent you a conformation email. Please check your email and click on the link to confirm your account. \n  If you don't see message, please check your junk folder!")

        # Welcome email
        subject = "Welcome to Your Family Website"
        message = "Hello " + newuser.first_name + "!! \n" + "Welcome to your your family's website!! \n We have sent you a confirmation email, please confirm your email address in order to activate your account."
        from_email = settings.EMAIL_HOST_USER
        to_list = [newuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Confirmation email
        current_site = get_current_site(request)
        email_subject = "Confirm your email in order to be able to log in."
        context = {
            'name':newuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
            'token': generate_token.make_token(newuser)
        }
                                                               
        
        message2 = render_to_string('email_confirmation.html',context)
        email = EmailMessage(email_subject,
                             message2,
                             settings.EMAIL_HOST_USER,
                             [newuser.email],
        )
        
        email.fail_silently = True
        email.send()
        



        return redirect('signin')  # Redirect member to sign in.

    return render(request,"signup.html")



# activate account

def activate(request,uidb64,token):   #for new user
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        newuser = User.objects.get(pk=uid)

    except (TypeError, ValueError,OverflowError,User.DoesNotExist):
        newuser = None
    
    if newuser is not None and generate_token.check_token(newuser, token):
        newuser.is_active = True
        newuser.save()
        login(request,newuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')








######################################################################################################33






@login_required
def updateProfile(request):
    # Retrieve or create a UserProfile for the logged-in user
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save(commit = False)
            if created:
                # Additional action when a new profile is created
                print(f"A new profile was created for user: {request.user}")
            
            return redirect('home')  # Redirect to the user's profile page
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'update_profile.html', {'form': form})



