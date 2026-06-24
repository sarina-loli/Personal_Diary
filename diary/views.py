from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

from .models import DiaryEntry
from .models import Profile

from .forms import RegisterForm
from .forms import DiaryEntryForm
from .forms import ProfileForm
from .forms import UserUpdateForm


def home(request):
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form': form})


@login_required
def dashboard(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    query = request.GET.get('q')
    if query:
        entries = entries.filter(title__icontains=query)
    date_filter = request.GET.get('date')
    if date_filter:
        entries = entries.filter(created_date__date=date_filter)
    total_entries = entries.count()
    recent_entries = entries[:5]
    happy_count = entries.filter(mood='Happy').count()
    excited_count = entries.filter(mood='Excited').count()
    calm_count = entries.filter(mood='Calm').count()
    neutral_count = entries.filter(mood='Neutral').count()
    sad_count = entries.filter(mood='Sad').count()
    angry_count = entries.filter(mood='Angry').count()

    context = {
        'entries': entries,
        'total_entries': total_entries,
        'recent_entries': recent_entries,
        'happy_count': happy_count,
        'excited_count': excited_count,
        'calm_count': calm_count,
        'neutral_count': neutral_count,
        'sad_count': sad_count,
        'angry_count': angry_count,
    }
    return render(request,'dashboard.html',context)


@login_required
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        user_form = UserUpdateForm( request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    context = {'user_form': user_form,'profile_form': profile_form,}
    return render(request,'profile.html',context)


@login_required
def add_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('dashboard')

    else:
        form = DiaryEntryForm()
    return render(request,'entry_form.html',{'form': form,'title': 'Add Entry'})


@login_required
def entry_detail(request, pk):
    entry = get_object_or_404(DiaryEntry,pk=pk,user=request.user)
    return render(request,'entry_detail.html',{'entry': entry})


@login_required
def edit_entry(request, pk):
    entry = get_object_or_404(DiaryEntry,pk=pk,user=request.user)

    if request.method == 'POST':
        form = DiaryEntryForm(request.POST,instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail',pk=entry.pk)

    else:
        form = DiaryEntryForm(instance=entry)
    return render(request,'entry_form.html',{'form': form,'title': 'Edit Entry'})

@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(DiaryEntry,pk=pk,user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('dashboard')
    return render(request,'entry_delete.html',{'entry': entry})