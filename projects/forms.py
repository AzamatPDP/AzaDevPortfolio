from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-indigo-500 transition-colors',
                'placeholder': 'Ismingiz'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-indigo-500 transition-colors',
                'placeholder': 'email@example.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-indigo-500 transition-colors',
                'placeholder': 'Xabar mavzusi'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-indigo-500 transition-colors resize-none',
                'placeholder': 'Xabaringizni yozing...',
                'rows': 5
            }),
        }
        labels = {
            'name': 'Ism',
            'email': 'Email',
            'subject': 'Mavzu',
            'message': 'Xabar',
        }
