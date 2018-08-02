from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def add_project(request):
           form1=Project_Form(request.POST or None)
           form2=Client_Form(request.POST or None)
           if form2.is_valid():
               form2.save()

           if form1.is_valid():
               obj = Client.objects.get(email=request.POST.get('email'))
               pro = Project.objects.create(project_name = request.POST.get('project_name'),
               url_name=request.POST.get('url_name'),
               domain_name=request.POST.get('domain_name'),
              #project_desrciption=request.POST.get('project_description'),
              attachment=request.POST.get('attachment'),
                                      client = obj)
               s = request.POST.getlist('technology')
               for x in s:
                   pro.technology.add(x)





           return render(request,'add_project.html',{'form1':form1,'form2':form2})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


"""def request_email(request):
    if request == 'GET':
        form = CustomAuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        Requested.objects.create(request_email = request.POST.get('request_email'))"""
