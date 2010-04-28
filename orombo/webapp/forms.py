# vim: ai sts=4 ts=4 et sw=4
from django import forms

class PostForm(forms.Form):
    '''Form for handling posts in Orombo'''
    title = forms.CharField(required=True)
    url = forms.URLField(required=True, initial='http://', verify_exists=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

class CommentForm(forms.Form):
    '''Form for capturing comments for posts'''
    comment = forms.CharField(required=True, widget=forms.Textarea)
    post = forms.DecimalField(required=True, widget=forms.HiddenInput)
