from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['is_done', 'created_ad', 'updated_at']

        labels  = {
            'title': 'Title'
        }

        widgets = {
            'title': forms.TextInput({
                'class': 'form-control mt-2',
                'placeholder': 'What needs to be done?'}),
            'due_date': forms.DateInput({
                'type': 'date',
                'class': 'form-control mt-2',
                'id': 'dueDate'
                }
            ),
            'description': forms.Textarea({
                'rows': 3,
                'class': 'form-control mt-2',
                'placeholder': 'What needs to be done?',
                }
            ),
            'priority': forms.RadioSelect({
                'class': 'form-check-input',
                }
            ),
            'category': forms.Select({
                'class': 'form-control mt-2',
                }
            ),
            'tag': forms.SelectMultiple({
                'class': 'form-control mt-2',
                'placeholder': 'Add tags '
                }
            ),
            
        }