from django import forms


class WorkerForm(forms.ModelForm):
    class Meta:
        widgets = {
            'work_experience': forms.widgets.DateInput(attrs={'type': 'date'}),
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }
