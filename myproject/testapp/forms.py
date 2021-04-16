from django import forms

from .models import Task, Client, COMPANY_CHOICES


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("text",)


class ClientForm(forms.Form):
    email = forms.EmailField(label="Электронная почта для обратной связи")
    name = forms.CharField(label="Имя клиента", max_length=100)
    company = forms.ChoiceField(label="Компания", choices=COMPANY_CHOICES)
    comment = forms.CharField(label="Комментарий", max_length=40)

    def clean_name(self):
        data = self.cleaned_data["name"]

        if Client.objects.filter(name=data).exists():
            raise forms.ValidationError(
                "Этого чувака мы уже знаем"
            )

        return data 