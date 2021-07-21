from django.contrib.auth.models import User
from django.shortcuts import render, redirect 
from django.http import HttpResponse,JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user, login, logout

from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
import sqlite3

# Create your views here.
from .models import *
from .forms import  CreateUserForm, newres
#from .filters import OrderFilter

def registerPageS(request):
    form= CreateUserForm()
    if request.method== 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"account was create for" +user)
            return redirect('logins')



    context={'form':form}
    return render(request,'registers.html',context)
def registerPageB(request):
    form= CreateUserForm()
    if request.method== 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"account was create for" +user)
            return redirect('loginb')



    context={'form':form}
    return render(request,'registerb.html',context)    
def loginPageS(request):
    if request.method =='POST':
        ur=request.POST.get("username")
        ps=request.POST.get("password")
        user=authenticate(request,username=ur,password=ps)
        if user is not None:
            login(request, user)
            return redirect('homes')
        else:
            messages.info(request,'Username or password is incorrect')
            #return redirect('login')    

    context={}
    return render(request,'logins.html',context)
def loginPageB(request):
    if request.method =='POST':
        ur=request.POST.get("username")
        ps=request.POST.get("password")
        user=authenticate(request,username=ur,password=ps)
        if user is not None:
            login(request, user)
            return redirect('homeb')
        else:
            messages.info(request,'Username or password is incorrect')
            #return redirect('login')    

    context={}
    return render(request,'loginb.html',context) 

def homes(request):
    conn = sqlite3.connect("E://Summer Project//.vscode//gg//src//cov//database.sqlite3")
    cur = conn.cursor()
    #cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #print(cur.fetchall())
    #context = None
    count = 0
    if request.method == 'POST':
        res = request.POST.get('res')
        cono = request.POST.get('cono')
        des=request.POST.get('des')
        qty = request.POST.get('qty')
        username = request.user.username
        lat=request.POST.get('lat')
        long=request.POST.get('long')

        print(res,cono,des,username,lat,long)
        cur.execute("insert into seller (res, cono, des,lat,long, uname, qty) values (?, ?, ?, ?, ?, ?, ?)",(res,cono,des,lat,long, username, qty))
        if(res is not "" and cono is not "" and des is not "" and username is not "" and lat is not "" and long is not "" ):
            conn.commit()
            cur.close()
            conn.close()
           # context = "Successfully Added!"
            messages.info(request,'Successfully Added!')

        else:
            messages.info(request,'Error! Insuffiscient Information')
            
          
            

        
   
    #print(context)       
    return render(request, 'homes.html')#, {'data': context})
            

   # print(res, cono, des)
          

def homeB(request):
    conn = sqlite3.connect("E://Summer Project//.vscode//gg//src//cov//database.sqlite3")
    
    class create_dict(dict): 
  
    # __init__ function 
        def __init__(self): 
            self = dict() 
          
    # Function to add key:value 
        def add(self, key, value): 
            self[key] = value

    mydict = create_dict()
    select_value = "SELECT * FROM seller"
    cursor = conn.cursor()
    cursor.execute(select_value)
    result = cursor.fetchall()

    for row in result:
        mydict.add(row[0],({"res":row[1],"cono":row[2],"des":row[3], "lat":row[4], "long":row[5], "uname":row[6], "qty":row[7]}))

    stud_json = json.dumps(mydict, indent=2, sort_keys=True)

    
    # details = request.GET.get('det')
    # print(details)

    # if details is not "" and details is not None:
    #     words = details.split(",")
    #     print(words[0], words[1], words[2])
    #     cursor.execute("INSERT INTO buyer (cono, com, sname) values(?,?,?)", (words[0], words[1], words[2]))
    #jsonfile = json.load(stud_json)
    

    #print(jsonfile)



    return render(request,'Homeb.html',{'data': stud_json}) 
    
            
def intro(request):
    return render(request,'intro.html',{})


def ViewS(request):
    conn = sqlite3.connect("E://Summer Project//.vscode//gg//src//cov//database.sqlite3")
    class create_dict(dict): 
  
    # __init__ function 
        def __init__(self): 
            self = dict() 
          
    # Function to add key:value 
        def add(self, key, value): 
            self[key] = value

    mydict = create_dict()

    username = request.user.username
    
    #query = "SELECT * FROM seller WHERE uname ="+" '"+"{}" +"' ".format(username)
    
   
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seller WHERE uname = ?", (username,))
    result = cursor.fetchall()
    #print(result)
    for row in result:
        mydict.add(row[0],({"res":row[1],"cono":row[2],"des":row[3], "lat":row[4], "long":row[5], "uname":row[6]}))

    
    stud_json = json.dumps(mydict, indent=2, sort_keys=True)
    print(mydict)

    
    
    return render(request, "ViewS.html", {'data2':stud_json})


def addButton(request):
    print("Button Working")

    return render(request,'Homeb.html') 