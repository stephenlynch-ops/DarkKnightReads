from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, removes auto generated labels
        and sets auto focus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_phone_number': 'Phone Number',
            'user_street_address1': 'Street Address 1',
            'user_street_address2': 'Street Address 2',
            'user_town_or_city': 'Town or City',
            'user_postcode': 'Postal / Zip Code',
            'user_county': 'County or State',
            'user_country': 'Country',
        }

        self.fields['user_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'user_country' and field != 'alter_ego':
                if self.fields[field].required:
                    placeholder = f'{placeholder[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border_black rounded-0 profile-form-input'
            self.fields[field].label = False
