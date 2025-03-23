
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def Home(request):
    return render(request,'base.html')


def Signup(request):
    if request.method == "POST":
        admin_email = request.POST.get('admin_email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if not admin_email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return render(request, 'signup.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if User.objects.filter(username=admin_email).exists():
            messages.error(request, "Admin Email is already registered.")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=admin_email, email=admin_email, password=password)
        user.is_staff = True  
        user.save()

        messages.success(request, "Signup successful! Please log in.")
        return redirect('/login')  

    return render(request, 'signup.html')





def Login(request):
    if request.method == "POST":
        ue = request.POST.get('admin_email', '').strip()
        up = request.POST.get('password', '').strip()

        if not ue or not up:
            messages.error(request, "All fields are required")
            return render(request, 'login.html')

        user = authenticate(username=ue, password=up)

        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            messages.error(request, "Invalid Email or Password")
            return render(request, 'login.html')

    return render(request, 'login.html')



def ulogout(request):
    logout(request)
    messages.success(request, "User logged out")
    return redirect('/')


def Bookentry(request):
    if request.method == 'POST':
        b_name = request.POST['book_name']
        b_author = request.POST['book_author']
        p_year = request.POST['publication_year']
        b_country = request.POST['country']

        book = Book.objects.create(
            book_name=b_name,
            book_author=b_author,
            publication_year=p_year,
            country=b_country
        )
        book.save()
        return redirect('/updatebook') 

    else:
        return render(request,'bookentry.html')


def Showbook(request):
    context={}
    all_books=Book.objects.all()
    context['books']=all_books
    return render(request,'base.html',context)

def Updatebook(request):
    context={}
    all_books=Book.objects.all()
    context['books']=all_books
    return render(request,'updatebook.html',context)

def Delete(request,bid):
    book=Book.objects.filter(id=bid)
    book.delete()
    return redirect('/updatebook')


def Update(request, bid):
    book = Book.objects.filter(id=bid).first()  

    if not book:
        return redirect('/showbook')  

    if request.method == "POST":
        book.book_name = request.POST['book_name']
        book.book_author = request.POST['book_author']
        book.publication_year = request.POST['publication_year']
        book.country = request.POST['country']
        book.save()
        return redirect('/showbook')  

    context = {'book': book}  
    return render(request, 'update.html', context)