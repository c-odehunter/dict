from import_export import widgets, fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Word
from .models import Definition
from .models import Category

admin.site.register(Word)
admin.site.register(Category)

class StoreWidget(widgets.ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        return self.model.objects.get_or_create(word_text = value)[0]

class DefinitionResource(resources.ModelResource):
    word_text = fields.Field(column_name='word_text',
                      attribute='word',
                      widget=StoreWidget(Word, 'word_text'))
    def __unicode__(self):
        return self.word_text.name
    class Meta:
        model = Definition
        fields = ('word_text','id', 'word', 'category', 'definition_text')

class DefinitionAdmin(ImportExportModelAdmin):
    list_display = ('word', 'category', 'definition_text')
    list_editable = ('definition_text',)
    search_fields = ['word__word_text', 'definition_text']
    resource_class = DefinitionResource
    skip_unchanged = True
    report_skipped = True

admin.site.register(Definition, DefinitionAdmin)
