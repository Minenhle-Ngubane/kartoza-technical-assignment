import requests
from django.conf import settings 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, UserProfileUpdateForm


# Home page with full screen map containing all users
def index(request):
    template = "user_profile/full_page_map.html"
    return render(request, template)


# User profile
@login_required
def user_profile(request):
    template = "user_profile/user_profile_page.html"
    return render(request, template)


# Edit user profile
@login_required
def edit_user_profile(request):

    if request.method == "POST":
        user_update_form         = UserUpdateForm(request.POST, instance=request.user)
        user_profile_update_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and user_profile_update_form.is_valid():
            user_update_form.save()
            instance = user_profile_update_form.save(commit=False)

            address = request.POST['address']
            status  = extract_lat_lng(address, instance)

            if status == "OK":
                messages.success(request, "Your profile has been successfully updated!")
                return redirect('user_profile')

            elif status == "ZERO_RESULTS":
                messages.warning(request, "No results returned, please check if address entered exists and try again.")
                return redirect('edit_user_profile')
            
            elif status == "OVER_DAILY_LIMIT":
                messages.error(
                    request, 
                    """
                    Error, this could be because of missing or invalid API key, 
                    billing has not been enabled on your account, 
                    a self-imposed usage cap has been exceeded or 
                    your provided method of payment is no longer valid (for example, a credit card has expired).
                    """
                    )
                return redirect('edit_user_profile')

            elif status == "OVER_QUERY_LIMIT":
                messages.error(request, "Error, you are over your quota")
                return redirect('edit_user_profile')

            elif status == "REQUEST_DENIED":
                messages.error(request, "Error, request denied.")
                return redirect('edit_user_profile')

            elif status == "INVALID_REQUEST":
                messages.error(request, "Error, query (address, components or latlng) is missing")
                return redirect('edit_user_profile')

            else:
                messages.error(request, "Error, request could not be processed due to a server error, please try again.")
                return redirect('edit_user_profile')

    else:
        user_update_form         = UserUpdateForm(instance=request.user)
        user_profile_update_form = UserProfileUpdateForm(instance=request.user.profile)

    context  = {
       "user_update_form": user_update_form,
       "user_profile_update_form":user_profile_update_form
    }

    template = "user_profile/edit_user_profile_page.html"
    return render(request, template, context)


# extract latitude and longitude from Geocoding API using user's address
def extract_lat_lng(address, instance):
    api_key   = settings.API_KEY
    endpoint  = f"https://maps.googleapis.com/maps/api/geocode/json?"
    params    = {
        "address": address,
        "key"    : api_key
    }

    response = requests.get(endpoint, params=params).json()
    status   = response["status"]

    if status == "OK":
        geometry           = response["results"][0]["geometry"]
        instance.latitude  = geometry["location"]["lat"]
        instance.longitude = geometry["location"]["lng"]
        instance.save()
        return status

    else:
        return status
  



    

 
