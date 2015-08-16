from django import forms

class SynthForm(forms.Form):
    CATEGORY_CHOICES = (
            ('mono', 'Monosynth'),
            ('poly', 'Polysynth'),
            ('dm', 'Drum machine'),
            )
    name = forms.CharField()
    issue_year = forms.DateField()
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    pic =  forms.ImageField()
    maker = forms.CharField()

    def post_synth(self):
        # send email using the self.cleaned_data dictionary
        pass
