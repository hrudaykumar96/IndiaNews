from django import forms
from .models import Category, Latest_News, Articles, Trending_News, Headlines
from tinymce.widgets import TinyMCE

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category Name','id': 'category-name'})
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Category.objects.filter(name__iexact=name).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Category already exists")
        return name

class Latest_News_Form(forms.ModelForm):
    class Meta:
        model=Latest_News
        fields=['title','description', 'image','category', 'is_acknowledge']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title','id': 'latest_news-title'}),
            'description':TinyMCE(attrs={'class':'form-control', 'placeholder':'Description', 'id':'latest_news-description'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control','id': 'latest_news-image'}),
            'category':forms.Select(attrs={'class':'form-select','id': 'latestnewscategory'}),
            'is_acknowledge':forms.CheckboxInput(attrs={'class':'form-check-input','id': 'latestnewscheck'})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all() 



class HeadlineForm(forms.ModelForm):
    class Meta:
        model=Headlines
        fields=['title','description', 'image','category', 'is_acknowledge']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title','id': 'headline-title'}),
            'description':TinyMCE(attrs={'class':'form-control', 'placeholder':'Description', 'id':'headline-description'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control','id': 'headlineimage'}),
            'category':forms.Select(attrs={'class':'form-select','id': 'headlinecategory'}),
            'is_acknowledge':forms.CheckboxInput(attrs={'class':'form-check-input','id': 'headline-checkmark'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()



class ArticlesForm(forms.ModelForm):
    class Meta:
        model=Articles
        fields=['title','description', 'image','category', 'is_acknowledge']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title','id': 'article-title'}),
            'description':TinyMCE(attrs={'class':'form-control', 'placeholder':'Description', 'id':'article-description'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control','id': 'articleimage'}),
            'category':forms.Select(attrs={'class':'form-select','id': 'articlecategory'}),
            'is_acknowledge':forms.CheckboxInput(attrs={'class':'form-check-input','id': 'articlecheckmark'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()



class Trending_News_Form(forms.ModelForm):
    class Meta:
        model=Trending_News
        fields=['title','description', 'image','category', 'is_acknowledge']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title','id': 'trending_news-title'}),
            'description':TinyMCE(attrs={'class':'form-control', 'placeholder':'Description', 'id':'trending_news-description'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control','id': 'trending_news-image'}),
            'category':forms.Select(attrs={'class':'form-select','id': 'trendingnewscategory'}),
            'is_acknowledge':forms.CheckboxInput(attrs={'class':'form-check-input','id': 'trendingnewschtrending'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()


class UpdateNewsForm(forms.Form):
    title = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Title', 'id':'updatenewstitle'
    }))
    description = forms.CharField(widget=TinyMCE(attrs={
        'class': 'form-control', 'placeholder': 'Enter Description', 'id':'updatenewsdescription'
    }))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'form-control', 'id':'updatenewsnewimage'
    }))
    category = forms.ChoiceField(choices=[], widget=forms.Select(attrs={
        'class': 'form-control', 'id':'updatenewscategory'
    }))
    is_acknowledge = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input', 'id':'updatenewsacknowledge'
    }))

    def __init__(self, *args, **kwargs):
        category_choices = kwargs.pop('category_choices', Category.objects.all().values_list('id', 'name'))
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = category_choices