from django import forms
from django.contrib.auth.forms import AuthenticationForm
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


class BootstrapClassMixin(object):
    def __init__(self, *args, **kwargs):
        super(BootstrapClassMixin, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if isinstance(field.widget, forms.TextInput) or isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                if isinstance(field.widget, forms.Textarea):
                    del field.widget.attrs['cols']
                    del field.widget.attrs['rows']


class SuggestionModelForm(BootstrapClassMixin, forms.ModelForm):
    class Meta:
        model = models.Suggestion
        fields = ['title', 'description']


class PostMessageForm(BootstrapClassMixin, forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['text']

class BSLoginForm(BootstrapClassMixin, AuthenticationForm):
    pass
