from django import forms
class Customer(forms.Form):
    firstname=forms.CharField(label="enter firstname",max_length=20)
    lastname=forms.CharField(label="enter lastname",max_length=20)
    email=forms.EmailField(label="enter email")
    phoneno=forms.CharField(label="enter contact no")