from django import forms

class TagWidget(forms.TextInput):
    template_name = "widgets/tag_widget.html"
