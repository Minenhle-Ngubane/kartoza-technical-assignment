from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# New user registration
def user_sign_up(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user     = authenticate(request, username=username, password=password)

            # Login the user after registration was successfull
            if user is not None:
                login(request, user)

            messages.success(request, f"Account created for {username}!")
            return redirect("edit_user_profile", user_id=user.id)
    else:
        form = UserCreationForm()

    context  = {
        "form": form,
    }

    template = "user_authentication/user_sign_up.html"
    return render(request, template, context)
