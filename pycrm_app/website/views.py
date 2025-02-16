from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Record
from .forms import SignUpForm, AddRecordForm

# Create your views here.
def home(request):
    records = Record.objects.all()
    return render(request, 'home.html', {'records':records})

def login_user(request):
        print("i am here")
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            #Authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "YOU HAVE LOGGED IN!!!!")
                return redirect('home')
            else:
                messages.success(request, "THERE WAS LOGIN ERROR....")
                return redirect('home')
        else:
            return render(request, 'login.html', {})
        

def logout_user(request):
    logout(request)
    messages.success(request, "YOU HAVE BEEN LOGGED OUT ....")
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
               form.save()
               #Auth & # login
               username = form.cleaned_data['username']
               password = form.cleaned_data['password1']

               user = authenticate(username=username, password=password)
               login(request, user)
               messages.success(request, "YOU HAVE SUCCESSFULLY REGISTERED!!!! WELCOME!!")
               return redirect('home')
            else:
                 messages.success(request, "Incorrect Details")
                 return redirect('register')     
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    

def user_details(request, pk):
    if request.user.is_authenticated:
         customRecord = Record.objects.get(id=pk)
         return render(request, "user-details.html", {'record': customRecord})
    else:
         messages.success(request, "YOU ARE NOT LOGGED IN. PLEASE LOGIN TO VIEW THE RECORD")
         return redirect("login")
    

def delete_user(request, pk):
    if request.user.is_authenticated:
        recordToDelete = Record.objects.get(id=pk)
        recordToDelete.delete()
        messages.success(request, "USER IS DELETED")
        return redirect("home")
    else:
        messages.success(request, "YOU ARE NOT LOGGED IN. PLEASE LOGIN TO VIEW THE RECORD")
        return redirect("login")

def add_user(request):
        form = AddRecordForm(request.POST or None)
        if request.user.is_authenticated:
            if request.method == "POST":
                if form.is_valid():
                    form.save()
                    messages.success(request, "Record Added....")
                    return redirect('home')
            
            return render(request, "add-user.html", {"form":form}) 
        else:
            messages.success(request, "YOU ARE NOT LOGGED IN. PLEASE LOGIN TO VIEW THE RECORD")
            return redirect("login")
          
def update_user(request, pk):
        if request.user.is_authenticated:
            current_record = Record.objects.get(id=pk)
            form = AddRecordForm(request.POST or None, instance=current_record)
            if form.is_valid():
                    form.save()
                    messages.success(request, "Record Updated....")
                    return redirect('home')
            return render(request, "update_user.html", {"form":form})
        else:
            messages.success(request, "YOU ARE NOT LOGGED IN. PLEASE LOGIN TO VIEW THE RECORD")
            return redirect("login") 
