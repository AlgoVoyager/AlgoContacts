from django.shortcuts import render,redirect
from .forms import ContactsForm,CreateUserForm
from .models import Contacts
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login as login_process
from django.contrib.auth.decorators import login_required
# from .filter import ContactFilter
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        register = CreateUserForm()
    
        if request.method == 'POST':
            register = CreateUserForm(request.POST)
            if register.is_valid():
                register.save()
                user = register.cleaned_data.get('username')
                messages.success(request,"Account created for " + user)
                return redirect('/login')
            
        context = {'register':register}
        return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
         
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login_process(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request,'login.html',context)
def logout_page(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def index(request):
    form = ContactsForm()
    stored = Contacts.objects.all()
    context = {'form': form,
    'stored': stored
    }
    if request.method == 'POST':
        print('index entered',request.method)
        form = ContactsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    
    
    return render(request,'index.html',context)

def update_contact(request,pk):
    contact = Contacts.objects.get(id=pk)
    form = ContactsForm(instance=contact)
    print('update entered')
    if request.method == 'POST':
        
        form = ContactsForm(request.POST,instance= contact)
        if form.is_valid:
            form.save()
            print('updated item')
            return redirect('/')
        else:
            return redirect('/')


    context = {'form': form,}
    return render(request,'update.html',context)
def delete_contact(request,pk):
    contact = Contacts.objects.get(id=pk)
    contact.delete()
    print('deleted one item')
    return redirect('/')