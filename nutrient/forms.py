from django import forms

from .models import DailyIntake

class DailyIntakeForm(forms.ModelForm):
    """一日の摂取量一覧"""

    class Meta:
        model = DailyIntake
        fields = ('protain', 'fat', 'carb', 'created_at')

        def clean_protain(self):
            value = self.cleaned_data['protain']
            if type(protain) is not int:
                raise forms.ValidationError('整数で入力してください')
            return value

        def clean_fat(self):
            value = self.cleaned_data['fat']
            if type(fat) is not int:
                raise forms.ValidationError('整数で入力してください')
            return value

        def clean_carb(self):
            value = self.cleaned_data['carb']
            if type(carb) is not int:
                raise forms.ValidationError('整数で入力してください')
            return value

        def clearn_created_at(self):