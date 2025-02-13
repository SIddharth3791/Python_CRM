from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login_user(request):
        print("i am here")
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(f"username : {username} ---- password : {password}")
            
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
            print("I am here")
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
    