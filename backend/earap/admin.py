from django.contrib import admin

from earap.models import Projects, Users, Steps, Actions, Elems

# Register your models here.
admin.site.register(Projects)
admin.site.register(Users)
admin.site.register(Actions)
admin.site.register(Steps)
admin.site.register(Elems)
