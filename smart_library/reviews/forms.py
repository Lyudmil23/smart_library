from django import forms

from smart_library.reviews.models import Review


class ReviewBookForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rate")

        widgets = {
            'rate': forms.NumberInput(
                attrs={
                    'min': "1",
                    'max': "5",
                    "step": "0.1",
                },
            ),
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Write your comment'
                }
            )
        }