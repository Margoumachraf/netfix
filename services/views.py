from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from users.models import Company, Customer, User

from .models import Service
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})






















def create(request):
    companies = User.objects.filter(is_company=True)
    company_usernames = [company for company in companies]

    if request.method == 'POST':
        form = CreateNewService(request.POST)
        print("Form is valid")
        print(form)
        # Get the cleaned data
        service_name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        price_hour = form.cleaned_data['price_hour']
        select_value = request.POST.get('field')
        # company_user = Company.objects.get(id=company_user_id)
        print(service_name)
        print(description)
        print(price_hour)
        print(select_value)
        # Ensure the company exists
        user_company = Company.objects.get(user_id=select_value)
        print("Company Info:", user_company.field)

        # Create the Service object
        Service.objects.create(
            name=service_name,
            description=description,
            price_hour=price_hour,
            company=user_company,
            field=user_company.field
        )
        # Add a success message and redirect
        messages.success(request, 'Service created successfully!')
        return redirect('/')  # Adjust the target URL to your success page


    if request.method == 'GET':
        # If GET request, render the empty form
        form = CreateNewService()
        return render(request, 'services/create.html', {
            'company_usernames': company_usernames,
            'form': form
        })










































































def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


def request_service(request, id):
    return render(request, 'services/request_service.html', {})
