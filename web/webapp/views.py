from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from webapp.models import Login,Profile
# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.POST.get('uname') and request.POST.get('upass'):
            uid=request.POST.get('uname')
            #print(uid)
            #print("I am here...",uid)
            up=request.POST.get('upass')
            request.session['user_id'] = uid
            #request.session['sname'] = uid
            if (Login.objects.filter(userid=uid).exists() and  Login.objects.filter(password=up).exists() ):
                print("reached")
                #return render(request, 'myhome.html')
                return redirect("/myhome")
            else:
                return render(request, 'home.html')

    else:
        return render(request, 'home.html') 
    


def register(request):
    #return render(request, 'register.html') 
    if request.method == 'POST':
        if request.POST.get('uname') and request.POST.get('upass') and request.POST.get('address') and request.POST.get('mobile'):
            login = Login()
            login.userid = request.POST.get('uname')
            login.password = request.POST.get('upass')
            login.save()
            
            reg=Profile()
            reg.userid=request.POST.get('uname')
            reg.upass=request.POST.get('upass')
            reg.address=request.POST.get('address')
            reg.mobile=request.POST.get('mobile')
            reg.email=request.POST.get('email')
            reg.gender=request.POST.get('gender')
            reg.dob=request.POST.get('date')
            reg.save()

            return render(request, 'register.html')

    else:
        return render(request, 'register.html')
    











def myhome(request):
    user_id = request.session['user_id']
    #myname = request.session.get('sname')
    print("user session:", user_id)

    return render(request, 'myhome.html',{"user_id" : user_id})




def viewall(request):
    profile = Profile.objects.all()
    return render(request, "viewall.html",{'profile': profile})



def edit(request):
    profile = Profile.objects.all()
    return render(request, "edit_user.html")
