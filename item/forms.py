from django import forms
from .models import Item

inp_classes = 'w-full py-6 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': inp_classes
            }),
            'name': forms.TextInput(attrs={
                'class': inp_classes
            }),
            'description': forms.Textarea(attrs={
                'class': inp_classes
            }),
            'price': forms.TextInput(attrs={
                'class': inp_classes
            }),
            'image': forms.FileInput(attrs={
                'class': inp_classes
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': inp_classes
            }),
            'description': forms.Textarea(attrs={
                'class': inp_classes
            }),
            'price': forms.TextInput(attrs={
                'class': inp_classes
            })
            # 'image': forms.FileInput(attrs={
            #     'class': inp_classes
            # })
            # 'is_sold': forms.Select(attrs={
            #     'class': inp_classes
            # },choices=[(True,"Yes"), (False,"No")]),
        }