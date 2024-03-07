from django import forms


class NameForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":"20", "id":"editor", "colums":"" , 
                                                           "class":"block w-full h-full resize-none  text-xs text-gray-900 font-medium text-gray-800 bg-white border-0 focus:ring-0 pt-8 px-8"}))