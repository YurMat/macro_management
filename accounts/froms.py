from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ObjectDoesNotExist

from .models import CustomUser

class RegisterForm(forms.ModelForm):
    """ユーザー登録画面用のフォーム"""

    class Meta:
        # 利用するモデルクラスを指定
        model = CustomUser
        # 利用するモデルのフィールドを指定
        fields = ('username', 'email', 'password',)
        # ウィジットを上書き
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'ユーザー名'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'パスワード'}),
        }

    password2 = forms.CharField(
        label='確認用パスワード',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': '確認用パスワード'}),
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['email'].widget.attrs = {'placeholder': 'メールアドレス'}

    def clean_username(self):
        value = self.clean_data['username']
        if len(value) < 3:
            raise forms.ValidationError(
                '(min_length)s文字以上で入力して下さい', params={'min_length': 3})
        return value

    def clean_email(self):
        value = self.cleaned_data['email']
        return value

    def clean_password(self):
        value = self.cleaned_data['password']
        return value

    def clean(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('パスワードと確認用パスワードが合致しません')
        # ユニーク成約を自動でバリデーションしてほしい場合はsuperのclean()を明示的に呼び出す
        super(RegisterForm,self.clean())

class LoginForm(forms.Form):
    username = UsernameField(
        label='ユーザー名',
        max_length=255,
        widget=forms.TextInput(attrs={'placehoider': 'ユーザー名', 'autofocus': True}),
    )

    password = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(attrs=｛'placeholder': 'パスワード'},render_value=True),
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean_password(self):
        value = self.cleaned_data['password']
        return value

    def clean_username(self):
        value = self.cleaned_data['username']
        if len(value) < 3:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力してください', params={'min_length': 3})
        return value

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = get_user_model().objects.get(username=username)
        except ObjectDoesNotExist:
            raise forms.ValidationError('正しいユーザー名を入力して下さい')
        if not user.check_password(password):
            raise forms.ValidationError('正しいユーザー名とパスワードを入力して下さい')
        self.user_cache = user

    def get_user(self):
        return self.user_cache

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'last_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widgets.attrs = {'placeholder': 'ユーザー名'}
        self.fields['email'].required = True
        self.fields['email'].widget.attrs = {'placeholder': 'メールアドレス'}
        # self.fields['password'].widget = forms.PasswordInput(attrs=)
        self.fields['last_name'].widget.attrs = {'placeholder': '苗字'}
        self.fields['first_name'].widget.attrs = {'placeholder': '名前'}

    def clean_username(self):
        value = self.cleaned_data['username']
        return value

    def clean_email(self):
        value = self.cleaned_data['email']
        return value
