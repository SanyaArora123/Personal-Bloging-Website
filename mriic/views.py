from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Blog, Contact_Us
from django.db.models import Q
# Create your views here.

#print(blog_info)
def home(request):
    blog_info = Blog.objects.all().order_by('-id')[:2]
    return render(request, 'mriic\home.html', {'blog_info': blog_info})

@login_required(login_url='loginUser')
def blogPage(request, Blog_id):
    print(Blog_id)
    blog = get_object_or_404(Blog, id = Blog_id)
    return render(request, r'mriic\blogPage.html',{'blog': blog})

@login_required(login_url='loginUser')
def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, r'mriic\blog.html',{'page_obj':page_obj})    

def about(request):
    return render(request, r'mriic\about.html')

def contact(request):
    if request.method == "GET":
        return render(request, 'mriic\contact.html')
    else:
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('message')
        data = Contact_Us(name = a, email = b, message = c)
        data.save()
        return render(request, 'mriic\contact.html', {'x':'Message Sent Successfully!!'})

def findBlog(request):
    if request.method == "POST":
        x = request.POST.get('blog_search')
        #print(x)
        mydata = Blog.objects.filter(Q(Blog_title__icontains = x) | Q(Blog_id__icontains = x) | Q(Category__icontains = x))
        #print(mydata)
        if mydata:
            return render(request,'mriic\home.html',{'blog_info':mydata})
        else:
            return render(request,'mriic\home.html',{'warning':'No Blog Found'})


def loginUser(request):
    if request.method == "GET":
        return render(request, 'mriic\loginUser.html',{'form':AuthenticationForm()})  
    else:
        a = request.POST.get("username")
        b = request.POST.get("password")
        user = authenticate(request, username = a, password = b) 
        if user is None:
            return render(request, 'mriic\loginUser.html',{'form': AuthenticationForm(),'error': 'Invalid Credentials'})
        else:
            login(request, user)
            return redirect('home')
def logOut(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
def signupUser(request):
    if request.method == "GET":
        return render(request, 'mriic\signupUser.html',{'form':UserCreationForm()})  
    else:
        a = request.POST.get("username")
        b = request.POST.get("password1")
        c = request.POST.get("password2")   
        if b == c:
            if(User.objects.filter(username = a)):
                return render(request, 'mriic\signupUser.html', {'form':UserCreationForm(),'error': 'User already exist Try Again'})
            else:
                user = User.objects.create_user(username = a, password = b)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            return render(request, 'mriic\signupUser.html', {'form':UserCreationForm(),'error':'Password Mismatch Try Again'})

    
