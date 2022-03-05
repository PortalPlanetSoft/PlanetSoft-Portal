from news.models import NewsArticle
from django import forms

ERROR_MESSAGES = {
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

