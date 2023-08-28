from django import forms
from feedback.models import Feedback


class FeedbackCreateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('subject', 'email', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})