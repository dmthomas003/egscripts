from django import forms
from library.models import Item, Category


## basic form to add item
## shown on userprofile if user is member of Contributor group
## need to adjust for new fields in Item model
class ContributionForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'category', 'text', 'description', 'location']
        widgets = {
            'text': forms.Textarea(attrs={'rows':4, 'cols':40}),
            'description': forms.Textarea(attrs={'rows':4, 'cols':40})
            }

