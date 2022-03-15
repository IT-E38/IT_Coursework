from django import forms
from vlog_app.models import User, UserProfile
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(min_length=4, max_length=30,
                               error_messages={
                                   'min_length': 'Username cannot be less than 4 characters',
                                   'max_length': 'Username cannot be more than 30 characters',
                                   'required': 'Cannot be empty',
                               },
                               widget = forms.TextInput(attrs={'placeholder': 'Username'})
                               )
    password = forms.CharField(min_length=8, max_length=30,
                                error_messages={
                                    'min_length': 'Password cannot be less than 8 characters',
                                    'max_length': 'Password cannot be more than 30 characters',
                                    'required': 'Cannot be empty',
                                },
                                widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
                                )
    password1 = forms.CharField(min_length=8, max_length=30,
                                error_messages={
                                    'min_length': 'Password cannot be less than 8 characters',
                                    'max_length': 'Password cannot be more than 30 characters',
                                    'required': 'Cannot be empty',
                                },
                                widget = forms.PasswordInput(attrs={'placeholder': 'Repeat Password'})
                                )
    email = forms.EmailField(required=False,
                             error_messages={
                                 'invalid': 'please enter the valid mail address',
                             },
                             widget = forms.EmailInput(attrs={'placeholder': 'Email address'})
                             )

    class Meta:
        model = User
        fields = ('username', 'password', 'email', )

    error_messages = {'password_mismatch': '两次密码不一致', }


class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'})
                          )
    class Meta:
        model = UserProfile
        fields = ('dob',)

class ProfileEditForm(forms.ModelForm):
    # nickname = forms.CharField(min_length=1,max_length=20,required=False,
    #                            error_messages={
    #                                'min_length': '昵称至少4个字符',
    #                                'min_length': '昵称不能多于20个字符',
    #                            },
    #                            widget=forms.TextInput())
    # avatar = forms.ImageField(required=False, validators=[avatar_file_size],
    #                           widget=forms.FileInput(attrs={'class' : 'n'}))
    email = forms.EmailField(required=False,
                             error_messages={
                                 'invalid': 'please enter the valid mail address',
                             },
                             widget = forms.EmailInput(attrs={'placeholder': 'Email address'})
                             )
    dob = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'})
                          )
    description= forms.CharField(
                               widget=forms.TextInput(attrs={'placeholder': 'description'})
                               )

    class Meta:
        model = UserProfile
        fields = [ 'email', 'dob', 'description']



