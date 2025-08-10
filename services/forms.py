from django import forms

from users.models import Company ,User


class CreateNewService(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, label='Description')
    price_hour = forms.DecimalField(
        decimal_places=2, max_digits=5, min_value=0.00)
    
    field = forms.ChoiceField(
        choices=[(user.id, user.username) for user in User.objects.filter(is_company=True)],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, choices='', **kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)

        if choices:
            self.fields['field'].choices = choices

        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'

        self.fields['name'].widget.attrs['autocomplete'] = 'off'
class RequestServiceForm(forms.Form):
    pass
