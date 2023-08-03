from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required #It helps in restricting user to access profile page to when logged out
from .forms import ProfileUpdateForm, UserUpdateForm
#Function Based Views
@login_required
def register(request):
    form = UserRegisterForm()
    if request.method == "POST": # If request method passed is post
        form = UserRegisterForm(request.POST) #Get the user information from form
        if form.is_valid(): #Check if form's all fields are filled correctly
            form.save() #save the user info in database
            username = form.cleaned_data.get('username') #Get the username of user
            messages.success(request, f'Account successfully created for {username}! Login Now') #To display msg when user is registered
            return redirect('login')   #once registration is done redirect page to log in
        else:
            form = UserRegisterForm() #if req method is not POST then do nothing
    return render(request, 'stackusers/register.html', {'form':form})
@login_required
def profile(request):
    return render(request, 'stackusers/profile.html')


@login_required
def profile_update(request):
    if request.method == "POST": 
        u_form = UserUpdateForm(request.POST, instance= request.user) 
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): 
            u_form.save()                           
            p_form.save()                     
            messages.success(request, f'Account Updated Successfully!')   
            return redirect('profile')                                     
    else:
                u_form = UserUpdateForm(request.POST, instance= request.user) 
                p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)



    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'stackusers/profile_update.html', context)
