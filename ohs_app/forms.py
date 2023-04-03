from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
# from django.forms import DateInput,TimeInput
# from django.forms import

from ohs_app.models import Login, Register, worker_register, complaints,schedule,work,Bill,CreditCard


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class login_form(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class cus_register(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        exclude = ('user',)


class worker_form(forms.ModelForm):
    class Meta:
        model = worker_register
        fields = '__all__'
        exclude = ('user',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = complaints
        fields = ('feedback',)


class ScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = schedule
        fields = ('date', 'start_time', 'end_time')

# form for model work
# for adding work for admin
class Work_form(forms.ModelForm):
    class Meta:
        model=work
        fields='__all__'

class addbill_form(forms.ModelForm):
    class Meta:
        model=Bill
        exclude=('status','paid_on')

class Creditcard_form(forms.ModelForm):
    card_no=forms.CharField(validators=[RegexValidator(regex='^.{16}$',message='Please enter a Valid Card No')])
    card_cvv=forms.CharField(widget=forms.PasswordInput,validators=[RegexValidator(regex='^.{3}$',message='Please enter a Valid CVV')])
    expiry_date=forms.DateField(widget=DateInput(attrs={'id': 'example-month-input'}))
    class Meta:
        model=CreditCard
        # exclude=('card_no','card_cvv','expiry_date')
        fields='__all__'