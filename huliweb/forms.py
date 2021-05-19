from django import forms

from huliweb.models import Inquiry


class InquiryForm(forms.Form):
    name = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    inquiry = forms.CharField(label=' ', widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    class Meta:
        model = Inquiry
        labels = {
            # 'name': "Name",
            # 'email': "Email",
            # 'inquiry': "Message",
            # 'phone': 'Phone Number'
        }
        fields = ('__all__')