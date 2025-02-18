from django import forms


# class ReviewForm(forms.Form):
#     username = forms.CharField(label='Your name', max_length=100, error_messages={
#         'required': 'Your name must not be empty',
#         'max_length': 'Please enter a shorter name'
#     })

#     review_text = forms.CharField(label='Your feedback', widget=forms.Textarea, max_length=200, error_messages={
#         'required': 'Your feedback must not be empty'
#     })
#     rating = forms.IntegerField(label='Your rating', min_value=1, max_value=5)

# Create a ModelForm for the Review model
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  # or ['', '', ] if i only want some fields
        # exclude = ['owner_comment']
        labels = {
            'username': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating'
        }
        error_messages = {
            'username': {
                'required': 'Your name must not be empty',
                'max_length': 'Please enter a shorter name'
            },
            'review_text': {
                'required': 'Your feedback'
            },
        }
