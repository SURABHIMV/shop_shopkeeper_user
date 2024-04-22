from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import admin
from .models import shop,shopkeeper,shop_user,added_shopkeeper,product
import os

# Create your views here.
signup_data = {}
def signupPage_shop(request):
    if request.method=='POST':
        shopname=request.POST.get('shopname')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password and confirm password are not same")
        else: 
          signup_data[shopname] = password1
          print(signup_data)
          print('shopname',shopname,password1,password2)
          my_shop=shop.objects.create(shop_Name=shopname)
          my_shop.save()
          return redirect('login_shop')
          #return HttpResponse("teacher data as been entered succesfully")
    return render(request,'signup_shop.html')

# Create your views here.
signup_data = {}
def signupPage_shopkeeper(request):
    if request.method=='POST':
        shopkeepername=request.POST.get('shopkeepername')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password and confirm password are not same")
        else: 
          signup_data[shopkeepername] = password1
          print('mmmmmmmmmmmmmmmmmm',signup_data)
          print('shopkeepername',shopkeepername,password1,password2)
          my_shopkeepername=shopkeeper.objects.create(shopkeeper_Name=shopkeepername)
          my_shopkeepername.save()
          return redirect('login_shopkeeper')
          #return HttpResponse("teacher data as been entered succesfully")
    return render(request,'signup_shopkeeper.html')


# Create your views here.
signup_data = {}
def signupPage_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password and confirm password are not same")
        else: 
          signup_data[username] = password1
          print(signup_data)
          print('username',username,password1,password2)
          my_user=shop_user.objects.create(user_Name=username)
          my_user.save()
          return redirect('login_user')
          #return HttpResponse("teacher data as been entered succesfully")
    return render(request,'signup_user.html')

def loginPage_shop(request):
    if request.method=='POST':
        shopname=request.POST.get('shopname')
        password1=request.POST.get('password')
        stored_password = signup_data.get(shopname)
        print(shopname, password1)
        print('stored_password',stored_password)
        if stored_password == password1:
            return redirect('shop_dashboard')
        else:
            return HttpResponse("Username Or Password is incorrect")


        #     #######################
        #     if shopname=='hospital_1':
        #       return redirect('adding_doc_patients')
        #     elif  hospitalname=='hospital_2':
        #       return redirect('adding_doc_patients1')
        #     elif hospitalname=='hospital_3':
        #       return redirect('adding_doc_patients2')
        # else:
        #     return HttpResponse("Username Or Password is incorrect")

    return render(request,'login_shop.html')

def loginPage_shopkeeper(request):
    if request.method=='POST':
        shopkeepername=request.POST.get('shopkeepername')
        password1=request.POST.get('password')
        stored_password = signup_data.get(shopkeepername)
        print(shopkeeper, password1)
        print('stored_password',stored_password)
        #     #####################
        #     if hospitalname=='hospital_1':
        #       return redirect('adding_doc_patients')
        #     elif  hospitalname=='hospital_2':
        #       return redirect('adding_doc_patients1')
        #     elif hospitalname=='hospital_3':
        #       return redirect('adding_doc_patients2')
        # else:
        #     return HttpResponse("Username Or Password is incorrect")

    return render(request,'login_shopkeeper.html')


def loginPage_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password')
        stored_password = signup_data.get(username)
        print(username, password1)
        print('stored_password',stored_password)
        if stored_password == password1:
            return redirect('user_dashboard')
        else:
            return HttpResponse("Username Or Password is incorrect")

        #     ############################
        #     if hospitalname=='hospital_1':
        #       return redirect('adding_doc_patients')
        #     elif  hospitalname=='hospital_2':
        #       return redirect('adding_doc_patients1')
        #     elif hospitalname=='hospital_3':
        #       return redirect('adding_doc_patients2')
        # else:
        #     return HttpResponse("Username Or Password is incorrect")

    return render(request,'login_user.html')

def shopkeeper_data(request):
    sh= shopkeeper.objects.all()
    context={'shopkeeper':sh}
    if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'add_shopkeeper':
                    shopkeeper_name = request.POST.get('shopkeepername')
                    shopkeeper_name1 = added_shopkeeper.objects.create(addedshopkeeper_Name=shopkeeper_name)
                    shopkeeper_name1.save()  
                    product_name=request.POST.get('productname')
                    productquantity=request.POST.get('productquantity')
                    prod=product.objects.create(product_Name=product_name,product_Quantity=productquantity)
                    prod.save()
                    context['shopkeeper_name']=shopkeeper_name  
                    print('nnnnnnnnnnnnnn',context)
    return render(request,'shop_dashboard.html',context)


def user(request):
    pd= product.objects.all()
    context={'product':pd}
    return render(request,'user_dashboard.html',context)