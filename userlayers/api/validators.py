from tastypie.validation import Validation
from mutant.models import ModelDefinition
from .naming import get_app_label_for_user

class FieldValidation(Validation):
    def is_valid(self, bundle, request=None):
        if hasattr(bundle.obj, 'model_def') and bundle.obj.model_def.fielddefinitions.filter(name=bundle.obj.name):
            return {'name': u'field with name "%s" already exists' % bundle.obj.name}
        return {}

class TableValidation(Validation):
    def is_valid(self, bundle, request=None):
        if ModelDefinition.objects.filter(app_label=get_app_label_for_user(bundle.request.user), name=bundle.obj.name):
            return {'name': u'table with name "%s" already exists' % bundle.obj.name}
        return {}        
