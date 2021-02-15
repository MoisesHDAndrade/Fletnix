from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Fletnix.apps.accounts.models import UserProfile
from .models import Profiles, WhoIsWatching
from .forms import ProfilesForm, WhoIsWatchinForm
from django.db.models import Q


def profile_add(request):
    accounts_number = Profiles.objects.filter(Q(user = request.user.user_profile))
    if len(accounts_number) <= 3:
        user = request.user.user_profile.id
        form = ProfilesForm()
        if request.method == 'POST':
            form = ProfilesForm(request.POST or None)
            if form.is_valid():
                data_from_form = Profiles(
                    user = form.cleaned_data['user'],
                    user_name = form.cleaned_data['user_name'],
                    user_age = form.cleaned_data['user_age'],
                    user_gender = form.cleaned_data['user_gender'],
                    user_avatar = form.cleaned_data['user_avatar']
                )
                data_from_form.save()
                messages.success(request, f'A new profile {data_from_form.user_name} was created')
                return redirect('user_profile:profile_detail')
    else:
        messages.error(request, 'Maximum number of profiles reached')
        return redirect('user_profile:profile_detail')

def profiles_edit(request, pk):
    profile = get_object_or_404(Profiles, pk = pk)
    form = ProfilesForm(request.POST or None, instance=profile)
    if request.method == 'POST' and form.is_valid():
        profile.save()
        messages.success(request, f'Profile {profile.user_name} was updated with success')
        return redirect('user_profile:profile_detail')
    return render(request, 'profile_edit.html', {'obj':profile})

def who_is_watching(request, pk):
    profile = get_object_or_404(Profiles, pk = pk)
    obj = WhoIsWatching.objects.all()
    
    if not obj:
        print('nao tem obj vou criar')
        obj = WhoIsWatching.objects.create(person = profile, person_avatar = profile.user_avatar, person_age = profile.user_age)
        return redirect('movies:index')
    else:
        
        obj = WhoIsWatching.objects.first()
        obj.person = profile
        obj.person_avatar = profile.user_avatar
        obj.person_age = profile.user_age
        obj.save()
       
        return redirect('movies:index')
    
    