from tastypie.validation import Validation
from mutant.models import ModelDefinition
from .naming import get_app_label_for_user

class FieldValidation(Validation):
    def is_valid(self, bundle, request=None):
        if bundle.obj.model_def.fielddefinitions.filter(name=bundle.data['name']):
            return {'name': u'field with name "%s" already exists' % bundle.data['name']}
        return {}

class TableValidation(Validation):
    def is_valid(self, bundle, request=None):
        if ModelDefinition.objects.filter(app_label=get_app_label_for_user(bundle.request.user), name=bundle.data['name']):
            return {'name': u'table with name "%s" already exists' % bundle.data['name']}
        return {}        
