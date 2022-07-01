from django import forms
from django.contrib.auth import get_user_model,password_validation
from django.forms import ValidationError, TextInput, EmailInput, PasswordInput
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator


User = get_user_model()


class RegisterForm(forms.ModelForm):
    re_password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را تکرار نمایید', 'type':'password', 'required':'', 'class':'e-field-inner'}),label='تکرار رمزعبور')
    
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'email', 'password',"re_password"]

        widgets = {
            'email': EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'type':'email', 'required':'', 'class':'e-field-inner'}),
            'password': PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'required':'', 'class':'e-field-inner', "id":"password"}),
        }
        labels = {
            'first_name' : _('نام'),
            'last_name' : _('نام خانوادگی'),
            'email' : _('ایمیل'),
            'password' : _('رمزعبور'),
            're_password' :'تکرار رمزعبور',
        }
        validators = {
            'email' : EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        }

    def clean_password(self):
        try:
            password_validation.validate_password(self.cleaned_data.get("password"), self.instance)
            return self.cleaned_data.get("password") 
        except ValidationError as error:
            raise forms.ValidationError("""
                                        1-این پسورد خیلی کوتاه است حداقل 8 کاراکتر
                                        2-پسورد خیلی ساده است
                                        3-پسورد فقط عدد است
                                        """)
    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password


    def save(self, commit=True) :
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()

        return user


class LoginForm(forms.Form):
        email=forms.CharField(max_length=16)
        password=forms.CharField(max_length=16,widget=PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'required':'', 'class':'e-field-inner'}),label='رمزعبور')
        fields = ['email','password']
        labels = {
            'email' : 'ایمیل',
            'password' : 'کلمه عبور',
        }



