from django.shortcuts import render,redirect
from .models import users 
from django.contrib import messages

# Create your views here.

def login(request):
        if request.method=='POST':
            username = request.POST['usr']
            password = request.POST['password']
            try:
                user = users.objects.get(username=username,password=password)
                if user is not None:
                    request.session['username'] = username
                    return redirect("/home")
                else:
                    messages.info(request,"Invalid User Name or Password")
                    return redirect("login")
            except users.DoesNotExist:
                user = None
                messages.info(request,"Invalid User Name or Password")
                return redirect("login")
                
        elif request.method=='GET':
            return render (request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        user = request.POST['usr']
        pswrd1 = request.POST['psrwd1']
        pswrd2 = request.POST['psrwd2']
        email = request.POST['email']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip']
        address = add1 + "," + add2 +"," + city +","+ state;

        user_object = users()
        
        if pswrd1!=pswrd2:
            messages.info(request,'Password Did Not Matched')
            return redirect('register')

        if users.objects.filter(email=email).exists():
            messages.info(request,'Email Already Taken')
            return redirect('register')
            
        if users.objects.filter(username=user).exists():
            messages.info(request,'Username Already Taken')
            return redirect('register')
        if len(zip_code) !=6:
            messages.info(request,'Invalid zipcode')
            return redirect('register')

        user_object.username = user
        user_object.password = pswrd1
        user_object.email = email
        user_object.address = address
        user_object.zip_code = zip_code
        
        user_object.save()
        return redirect('/home')

        print("Object Inserted")


    if request.method == 'GET':
        return render(request,'accounts/register.html')

def logout(request):
        del request.session['username']
        return redirect('login')


    