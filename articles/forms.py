from django import forms
from .models import Article


class _ArticleCreateForm(forms.Form):
    title = forms.CharField(max_length=221)
    content = forms.CharField(max_length=221)



class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
