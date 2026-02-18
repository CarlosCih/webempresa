from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo electrónico', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))