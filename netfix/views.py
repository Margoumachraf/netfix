from django.shortcuts import render

from users.models import User, Company
from services.models import Service


def home(request):
    return render(request, 'users/home.html', {'user': request.user})


def customer_profile(request):
    pass


def company_profile(request, name):
    # fetches the company user and all of the services available by it
    user = User.objects.get(username=name)
    # company=Company.objects.get(user=user)
    # print("Company:", company)
    # services = Service.objects.filter(
    #     company.fi=Company.objects.get(id=user.id)).order_by("-date")

    return render(request, 'users/profile.html', {'user': user})
