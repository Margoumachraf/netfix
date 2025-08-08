from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView

from .forms import CustomerSignUpForm, CompanySignUpForm, UserLoginForm
from .models import User, Company, Customer


def register(request):
    return render(request, 'users/register.html')



class CustomerSignUpView(CreateView):
    model = Customer
    form_class = CustomerSignUpForm
    template_name = 'users/register_customer.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print(form)
        user = form.save()
        login(self.request, user)

        # Debug: print submitted data
        # print("Customer Signup POST data:", self.request.POST)

        return redirect('/')  # Replace 'home' with your actual success page

class CompanySignUpView(CreateView):
    model = User  # or Company if you created a separate model
    form_class = CompanySignUpForm
    template_name = 'users/register_company.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print("Company Signup POST data:", self.request.POST)

        user = form.save()
        login(self.request, user)

        # Example of accessing data from the form/request
        company_name = self.request.POST.get('company_name')
        email = self.request.POST.get('email')
        print("Company Name:", company_name)
        print("Email:", email)

        return redirect('home')  # Replace 'home' with your actual success page



def LoginUserView(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})