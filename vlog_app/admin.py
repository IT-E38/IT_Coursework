from django.apps import apps
from django.contrib import admin
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField



class AdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.list_filter = [field.name for field in model._meta.fields]
        super(AdminMixin, self).__init__(model, admin_site)


models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (AdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
