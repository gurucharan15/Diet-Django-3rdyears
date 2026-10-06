import re
from django import forms

class StudentForm(forms.Form):
    # Field 1: Name
    name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter alphabets only'})
    )

    # Field 2: Phone number
    phone = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(attrs={'placeholder': '10 digits starting with 6-9'})
    )

    # Regex validation for Name (Alphabets and spaces only)
    def clean_name(self):
        name = self.cleaned_data['name']
        pattern = r'^[a-zA-Z\s]+$'
        if not re.match(pattern, name):
            raise forms.ValidationError("Invalid Name: Only alphabets allowed.")
        return name

    # Regex validation for Phone (10 digits starting with 6, 7, 8, or 9)
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = r'^[6-9]\d{9}$'
        if not re.match(pattern, phone):
            raise forms.ValidationError("Invalid Phone: Must be 10 digits starting with 6-9.")
        return phone
