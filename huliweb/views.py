from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View

from huliweb.forms import InquiryForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class SubView(View):
    def get(self, request):
        form = InquiryForm()
        context = {'form':form}
        return render(request, 'sublimation.html',context)

    def post(self, request, *args, **kwargs):
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['inquiry']
            email = form.cleaned_data['email']

            email = EmailMessage(
                subject='Inquiry from ' + str(email),
                body='Name: ' + str(name) + '\n'
                     + 'message: ' + str(message) + '\n'
                     + 'email: ' + str(email) + '\n'
                     + 'phonenumber: ' + str(phone) + '\n'
                ,
                from_email='huliwatersportapparel@gmail.com',
                to=['huliwatersportapparel@gmail.com']

            )
            email.send()

            return redirect(reverse('huliweb:index'))