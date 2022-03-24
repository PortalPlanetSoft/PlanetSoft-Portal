from django import forms

from news.constants import ERROR_MESSAGES, LABEL_TEXT
from news.models import NewsArticle

LABEL_TEXT = {
    "headline": "Naslov",
    "content": "Sadržaj",
    "image": "Slika"
}


class AddNewsArticleForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = NewsArticle
        fields = {'headline', 'content', 'image'}
        error_messages = ERROR_MESSAGES

        widgets = {
            'headline': forms.TextInput(attrs={'placeholder': 'Naslov'}),
            'content': forms.Textarea(attrs={'placeholder': 'Sadržaj'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in LABEL_TEXT.items():
            self.fields[key].label = value
