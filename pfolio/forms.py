from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30 , widget=forms.TextInput(attrs={'placeholder': "Name"}))
    email = forms.EmailField(max_length=254 , widget=forms.TextInput(attrs={'placeholder': "Email"}))
    subject = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'placeholder': "Subject"}))
    message = forms.CharField(
        max_length=200,
        widget=forms.Textarea(attrs={'placeholder': 'Message'}),
        help_text='Write here your message!',
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')
        if not name and not email and not subject and not message:
            raise forms.ValidationError('You have to write something!')