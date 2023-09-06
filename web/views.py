from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.conf import settings

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('signup')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} Already Taken")
                return redirect('signup')
            else:
                user = MyUser.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'Registered succesefull.')
                return redirect('signin')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('signup')

    else:
        return render(request, 'web/signup.html')

def signin(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Loged in succesefull.')
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('signin')

    else:
        return render(request, 'web/signin.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Loged out succesefull.')
    return redirect('signin')


def home(request):
    return render(request, 'web/home.html')
def aboutus(request):
    return render(request, 'web/aboutus.html')
def base(request):
    return render(request, 'web/base.html')
def project(request):
    return render(request, 'web/project.html')
def strategic(request):
    return render(request, 'web/strategic.html')
def contactus(request):
    return render(request, 'web/contactus.html')
def contactpost(request):
    contactpost = ContactForm()
    if request.method == "POST":
        Full_Name = request.POST.get('Full_Name')
        Email = request.POST.get('Email')
        Message = request.POST.get('Message')
        Phone = request.POST.get('Phone')
        contactpost = ContactForm(request.POST, files=request.FILES)
        if contactpost.is_valid():
            contactpost.save()
            return redirect('contactpost')
    context={
        "contactpost":contactpost
    }
    return render(request, 'web/contactpost.html',context)
@login_required(login_url='signin')
def contactlist(request):
    contactlist = Contact.objects.all()
    countmessage= Contact.objects.all().count()
    context={
        "contactlist":contactlist,
        "countmessage":countmessage
    }
    return render(request, 'web/contactlist.html', context)
@login_required(login_url='signin')
def viewcontact(request, id):
    contact = Contact.objects.get(id=id)
    
    context = {"contact":contact}
    return render(request, 'web/viewcontact.html', context)
@login_required(login_url='signin')
def deletecontact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        contact.delete()
        return redirect('contactlist')
    
    context = {"contact":contact}
    return render(request, 'web/deletecontact.html', context)

@login_required(login_url='signin')
def files(request):
    files = MyfileForm()
    if request.method == "POST":
        files = MyfileForm(request.POST, files=request.FILES)
        if files.is_valid():
            files.save()
            messages.info(request, 'Document added succesefull.')
            return redirect('files')
        return redirect("home")
    context={
        "files":files
    }
    return render(request, 'web/files.html',context)

@login_required(login_url='signin')
def filesdisplay(request):
    filesdisplay = Myfile.objects.all()
    countfile= Myfile.objects.all().count()
    context={
        "filesdisplay":filesdisplay,
        "countfile":countfile
    }
    return render(request, 'web/filesdisplay.html', context)

@login_required(login_url='signin')
def viewfiles(request, id):
    fileview = Myfile.objects.get(id=id)
    
    context = {"fileview":fileview}
    return render(request, 'web/viewfiles.html', context)

@login_required(login_url='signin')
def deletefiles(request, id):
    filesdelete = Myfile.objects.get(id=id)
    # if request.method == "POST":
    filesdelete.delete()
    messages.info(request, 'Document deleted succesefull.')
    return redirect('filesdisplay')
    
    # context = {"filesdelete":filesdelete}
    # return render(request, 'web/deletefiles.html', context)

@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'web/dashboard.html')

@login_required(login_url='signin')
def governance(request):
    governance = GovernanceForm()
    if request.method == "POST":
        governance = GovernanceForm(request.POST, files=request.FILES)
        if governance.is_valid():
            governance.save()
            messages.info(request, 'Leader added succesefull.')
            return redirect('governance')
        return redirect("home")
    context={
        "governance":governance
    }
    return render(request, 'web/governance.html',context)

# @login_required(login_url='signin')
# def viewleader(request, id):
#     leaderview = Governance.objects.get(id=id)
    
#     context = {"leaderview":leaderview}
#     return render(request, 'web/viewleader.html', context)

@login_required(login_url='signin')
def deleteleader(request, id):
    leaderdelete = Governance.objects.get(id=id)
    # if request.method == "POST":
    leaderdelete.delete()
    messages.info(request, 'Leader deleted succesefull.')
    return redirect('leaderdisplay')
    
    # context = {"leaderdelete":leaderdelete}
    # return render(request, 'web/deleteleader.html', context)
    
@login_required(login_url='signin')
def leaderdisplay(request):
    leaderdisplay = Governance.objects.all()
    countleader= Governance.objects.all().count()
    context={
        "leaderdisplay":leaderdisplay,
        "countleader":countleader
    }
    return render(request, 'web/leaderdisplay.html', context)