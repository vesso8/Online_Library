import os

from django import forms

from online_library.library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image')
        widgets ={
            'first_name' : forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'URL'
                }
            ),
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image')

class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image')

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        widgets = {
            'title': forms.TextInput(
                attrs= {
                    'placeholder': 'Title'
                }
            ),
            'description': forms.Textarea(
                attrs= {
                    'placeholder': 'Description',
                    'rows': 4,
                }
            ),
            'image': forms.TextInput(
                attrs= {
                    'placeholder': 'Image'
                }
            ),
            'type': forms.TextInput(
                attrs= {
                    'placeholder': 'Fiction, Novel, Crime..'
                }
            ),
        }

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')