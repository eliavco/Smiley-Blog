from django import forms
from post_app.models import Post,CommentForm

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        firlds = ('author','title','text',)

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text' :forms.TextArea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }