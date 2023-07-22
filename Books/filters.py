from django_filters import DateTimeFilter,FilterSet ,ChoiceFilter
from django import forms
from .models import Books


class BookFilter(FilterSet):
    category=ChoiceFilter(choices=Books.Category.choices)
    language=ChoiceFilter(choices=Books.Languages.choices)
    publication_date=DateTimeFilter(widget=forms.DateInput(attrs={"type":"date"}),lookup_expr='date__exact')

    class Meta:
        model=Books
        fields=['category','language','publication_date']