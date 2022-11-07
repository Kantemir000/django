from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    #name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не болеее 15 символов")
    age = forms.IntegerField(label="Возраст")
    email=forms.EmailField(label="Электронный адрес")
    text=forms.RegexField("Введите текст")
    url_text=forms.URLField(label="Введите URL")
    vyb = forms.NullBooleanField(label="Вы поедите в сочи?")
    basket = forms.BooleanField(label="Положить товар в корзину?")
    file_path=forms.FilePathField(label="Выберите файл", path="D:\document\Инф. безопасность")
    file=forms.FileField(label="Файл")
