from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

User = get_user_model()

class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=500, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address',
        'id': 'login-email'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'login-password'
    }))

    def clean_username(self):
        email = self.cleaned_data.get('username')
        if not email:
            raise forms.ValidationError("Please enter your email address")
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is not registered")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Please enter your password")
        return password

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                if CustomUser.objects.filter(email=email).exists():
                    raise forms.ValidationError("Incorrect password")
                else:
                    raise forms.ValidationError("Invalid email or password")
            elif not user.is_active:
                raise forms.ValidationError("This account is inactive")
        return super().clean()

        



class UserSignUpform(UserCreationForm):
    name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Full Name',
        'id': 'signup-name'
    }))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address',
        'id': 'signup-email'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'signup-password'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
        'id': 'signup-cnfpassword'
    }))

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        validate_password(password1, self.instance)
        return password1

    def save(self, commit=True):
        user = super(UserSignUpform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        if commit:
            user.save()
        return user
    

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Old Password',
            'id': 'password-old'
        })
    )
    new_password1 = forms.CharField(
        label='New Password', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password',
            'id': 'password-password'
        })
    )
    new_password2 = forms.CharField(
        label='Confirm New Password', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password',
            'id': 'password-cnfpassword'
        })
    )

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Old password is incorrect")
        return old_password
    


    

class CustomPasswordResetForm(SetPasswordForm):
    email = forms.EmailField(
        label="Email", 
        max_length=500, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address','id': 'reset-email'})
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password','id': 'reset-password'}),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password','id': 'reset-cnfpassword'}),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email not registered")
        return email
    
    def save(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        new_password = self.cleaned_data.get('new_password1')

        user = get_user_model().objects.get(email=email)
        user.password = make_password(new_password)
        user.save()
        return user
    

class AdminSignUpform(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Full Name',
        'id': 'adminname'
    }))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address',
        'id': 'adminemail'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'adminpassword'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
        'id': 'admincnfpassword'
    }))

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['name','email','role']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'Enter Name', 'id':'updatename'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control','placeholder':'Enter Email Address', 'id':'updateemail'
            }),
            'role':forms.Select(attrs={
                'class':'form-select', 'id':'updaterole',
            })
        }
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if CustomUser.objects.filter(email__iexact=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Email Already Registered")
        return cleaned_data
    


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email','image','description','facebook','linkedin','instagram','twitter','skype']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name', 'id':'profileName'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email Address', 'id':'profileEmail'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control', 'id':'profileNewImage'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Description','required':False, 'id':'profileDescription'}),
            'facebook':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Facebook url', 'required':False, 'id':'profileFacebook'}),
            'linkedin':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Linkedin url', 'required':False, 'id':'profileLinkedin'}),
            'instagram':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Instagram url', 'required':False, 'id':'profileInstagram'}),
            'twitter':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Twitter url', 'required':False, 'id':'profileTwitter'}),
            'skype':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Skype url', 'required':False, 'id':'profileSkype'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email cannot be empty')
        if CustomUser.objects.filter(email__iexact=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Email is already registered')
        return email
    

    def clean_name(self):
        name=self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Name Cannot be Empty')
        return name