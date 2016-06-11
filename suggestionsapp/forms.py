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
                if isinstance(field.widget, forms.TextInput):
                    if field.label is not None:
                        field.widget.attrs['placeholder'] = unicode(field.label)
                    else:
                        field.widget.attrs['placeholder'] = unicode(pretty_name(field_name))
                    field.label = ""


class SuggestionModelForm(PlaceholdersMixin, forms.ModelForm):
    model = models.Suggestion
    fields = ['title', 'description']
