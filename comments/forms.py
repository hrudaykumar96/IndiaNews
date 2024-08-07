from django import forms
from .models import Comments, Reply

class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['text']
        widgets={
            'text':forms.Textarea(attrs={
                'class':'form-control', 'placeholder':'Comments', 'required':'required', 'id':'comments'
            })
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model=Reply
        fields=['text']
        widgets={
            'text':forms.Textarea(attrs={
                'class':'form-control', 'placeholder':'Reply', 'required':'required', 'id': 'unique_id_for_my_field'
            })
        }