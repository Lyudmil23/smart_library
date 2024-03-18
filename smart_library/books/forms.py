from django import forms

from smart_library.books.models import RentBook


class RentBookForm(forms.ModelForm):
    period_start = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
        })
    )
    period_end = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
        })
    )

    class Meta:
        model = RentBook
        fields = ('period_start', 'period_end')