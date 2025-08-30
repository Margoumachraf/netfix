from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Service, Type
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, 'services/single_service.html', {'service': service})


def create(request):
    if request.method == 'POST':
        form = CreateNewService(request.POST)
        if form.is_valid():
            # Get the cleaned data
            service_name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price_hour = form.cleaned_data['price_hour']
            field_id = form.cleaned_data['field']  # assuming 'field' is a ModelChoiceField
            
            # Get the Type instance
            field_instance = get_object_or_404(Type, id=field_id)
            

            # Create the Service
            Service.objects.create(
                name=service_name,
                description=description,
                price_hour=price_hour,
                field=field_instance
            )
            
            messages.success(request, 'Service created successfully!')
            return redirect('/')  # change to your desired success URL
        else:
            messages.error(request, 'Please correct the errors below.')
    
    else:
        form = CreateNewService()

    return render(request, 'services/create.html', {'form': form})


def service_field(request, field):
    # Normalize the field name
    field_name = field.replace('-', ' ').title()
    field_instance = get_object_or_404(Type, name=field_name)
    services = Service.objects.filter(field=field_instance)
    return render(request, 'services/field.html', {'services': services, 'field': field_name})


def request_service(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, 'services/request_service.html', {'service': service})
