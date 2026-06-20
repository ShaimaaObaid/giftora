from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.db.models import Q

from .models import Gift, Recommendation


def home(request):
    trending_gifts = Gift.objects.filter(is_trending=True)[:4]

    context = {
        'trending_gifts': trending_gifts
    }

    return render(request, 'main/home.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        messages.error(request, 'Invalid email or password')
        return redirect('/login/')

    return render(request, 'main/login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if len(first_name) < 2:
            messages.error(request, 'First name must be at least 2 characters')
            return redirect('/register/')

        if len(last_name) < 2:
            messages.error(request, 'Last name must be at least 2 characters')
            return redirect('/register/')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('/register/')

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters')
            return redirect('/register/')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('/register/')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        login(request, user)
        return redirect('/')

    return render(request, 'main/register.html')


def suggestions(request):
    gifts = Gift.objects.all()

    context = {
        'gifts': gifts
    }

    return render(request, 'main/suggestions.html', context)


def about(request):
    return render(request, 'main/about.html')


def gift_search_api(request):
    query = request.GET.get('q', '')

    gifts = Gift.objects.filter(
        Q(name__icontains=query) |
        Q(category__icontains=query) |
        Q(occasion__icontains=query) |
        Q(recipient_type__icontains=query)
    )

    data = []

    for gift in gifts:
        data.append({
            'name': gift.name,
            'description': gift.description,
            'price': str(gift.price),
            'image': gift.image,
        })

    return JsonResponse({'gifts': data})


def find_gift(request):
    gifts = None
    searched = False

    recipient_type = request.GET.get('recipient_type')
    occasion = request.GET.get('occasion')
    budget = request.GET.get('budget')

    if recipient_type and occasion and budget:
        searched = True

        gifts = Gift.objects.filter(
            recipient_type__iexact=recipient_type,
            occasion__iexact=occasion,
            price__lte=budget
        )

        if request.user.is_authenticated:
            Recommendation.objects.create(
                user=request.user,
                occasion=occasion,
                budget=budget,
                recipient_type=recipient_type
            )

    context = {
        'gifts': gifts,
        'searched': searched
    }

    return render(request, 'main/find_gift.html', context)
