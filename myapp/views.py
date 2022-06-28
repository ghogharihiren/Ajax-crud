from django.http import JsonResponse
from django.shortcuts import render
from .models import*
from .forms import*
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    user=User.objects.all()
    form=UsercreateForm()
    return render(request,'index.html',{'uid':user,'form':form})

def add(request):
    if request.method == "POST":
        data=UsercreateForm(request.POST)
        if data.is_valid():
            sid = request.POST.get('stuid')
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            password=request.POST['password']
            if(sid == ''):
                user=User(name=name,email=email,phone=phone,password=password)
            else:
                user=User(id=sid,name=name,email=email,phone=phone,password=password)
            user.save()
            std=User.objects.values()
            s=list(std)
            return JsonResponse({'status':200,'user':s})
        else:
            return JsonResponse({'status':400})
        
def delete(request):
    if request.method =="GET":
        id=request.GET.get('sid')
        user=User.objects.get(pk=id)
        user.delete()
        return JsonResponse({'status':200})
    return JsonResponse({'status':400})
          
            
   
# def edit(request):
#     if request.method =="POST":
#         id=request.POST.get('sid')
#         user=User.objects.get(pk=id)
#         form1=EditUserForm(instance=user)
#         form=EditUserForm(instance=user,data=request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'status':200,'data':form1})
#         else:
#             return JsonResponse({'status':400})
        
def edit(request):
    if request.method == "POST":
        id=request.POST.get('sid')
        user=User.objects.get(pk=id)
        user_data={'id':user.id,'name':user.name,'email':user.email,'phone':user.phone}
        return JsonResponse(user_data)
    