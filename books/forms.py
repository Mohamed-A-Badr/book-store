from django import forms
from .models import Book
from .validators import validate_isbn


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "isbn", "photo"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter book title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter book description"}
            ),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "isbn": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter ISBN"}
            ),
        }

    def clean_isb(self):
        isbn = self.cleaned_data["isbn"]
        validate_isbn(isbn)

        return isbn
