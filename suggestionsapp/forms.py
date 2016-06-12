from django import forms
from suggestionsapp import models


def pretty_name(name):
    """Converts 'first_name' to 'First name'"""
    if not name:
        return ''
    return name.replace('_', ' ').capitalize()


class PlaceholdersMixin(object):
    def __init__(self, *args, **kwargs):
        super(PlaceholdersMixin, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                print field.widget
                if isinstance(field.widget, forms.TextInput) or isinstance(field.widget, forms.Textarea):
                    if field.label is not None:
                        field.widget.attrs['placeholder'] = unicode(field.label)
                    else:
                        field.widget.attrs['placeholder'] = unicode(pretty_name(field_name))
                    field.label = ""
                # Bootstrap thing
                field.widget.attrs['class'] = 'form-control'


class SuggestionModelForm(PlaceholdersMixin, forms.ModelForm):
    class Meta:
        model = models.Suggestion
        fields = ['title', 'description']
