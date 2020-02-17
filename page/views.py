from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import Rental
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView

# Create your views here.

def home(request):
  obj = Rental.objects.all()
  context = {'obj':obj}
  return render(request,'index.html',context)


def profile(request):
  context = {}
  return render(request,'profile.html',context)


def login(request):
  if request.method =='POST':
    uname = request.POST['username']
    pwd = request.POST['password']

    user = auth.authenticate(username=uname,password=pwd)
    if user is not None:
      auth.login(request,user)
      messages.success(request,', Logged in successfully!')
      return redirect('/')

    else:
      messages.error(request,'invalid credentials')
      return redirect('login')
  else: 
    return render(request,'registration/login.html')


def logout(request):
  auth.logout(request)
  messages.success(request,', logged out successfully!')
  return redirect('/')



def register(request):
  if request.user.is_authenticated:
    return redirect('home')
  elif request.method == 'POST':
    fname = request.POST['fname']
    lname = request.POST['lname']
    uname = request.POST['uname']
    email = request.POST['email']
    pwd1 = request.POST['pwd1']
    pwd2 = request.POST['pwd2']

    if pwd1==pwd2:
      if User.objects.filter(username=uname).exists():
          messages.warning(request,', Username Taken!')
          return redirect('register')
      elif User.objects.filter(email=email).exists():
          messages.warning(request,', Email Taken!')
          return redirect('register')
      else:    
        user = User.objects.create_user(username=uname,password=pwd1,email=email,first_name=fname,last_name=lname)
        user.save()
        auth.login(request,user)
        messages.success(request,',  Registered and logged in successfully!')
        return redirect('/')
    else:
      messages.error(request,'Password not matching!')
      return redirect('register')  
  else:
    return render(request,'registration/register.html')


# class PropertyCreateView(CreateView):
#   model=Rental
#   form = PropertyForm

class PropertyCreateView(CreateView):
    model = Rental
    fields = ('name', 'img','desc','price')
    template_name = 'create.html'
    success_url = '/'