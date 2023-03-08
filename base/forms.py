from django import forms

class PostCv(forms.Form):
    designation= (
        ("Manager", "Manager"),
        ("Cashier", "Cashier"),
        ("Operator", "Operator"),
    )

    name = forms.CharField(label='Name of Applicant', max_length=50)
    address = forms.CharField(label='Address', max_length=100)
    Designation = forms.ChoiceField(choices=designation)
    phoneno = forms.IntegerField()
    time_submit = forms.TimeField()