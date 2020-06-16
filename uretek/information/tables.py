import django_tables2 as tables
from .models import Person
from django.utils.html import format_html



class PersonTable(tables.Table):

    class Meta:
        model = Person
        fields = ('name0','name', 'name1')

    def render_name(self, value, record):
        return format_html(r"%s" % value, record.name)

    def render_name1(self, value, record):
        return format_html(r"%s" % value, record.name1)
    def render_name0(self, value, record):
        return format_html(r"%s" % value, record.name0)


