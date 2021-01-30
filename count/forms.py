from django import forms

class CountText(forms.Form):
    txt =forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), max_length=10000, label='Enter the text', required=False)

def __init__(self, *args, **kwargs):
    super(CountText,self).__init__(*args, **kwargs)
