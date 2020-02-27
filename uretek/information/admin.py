from django.contrib import admin
from .models import \
    Subnavigator,Navconstruct,Subsubnav,Social,Footer,Text,Footercont,Page,Slider,Pagenext, Projects, Example, Pictures, Short, Pageproject

admin.site.register(Subnavigator)
admin.site.register(Navconstruct)
admin.site.register(Subsubnav)
admin.site.register(Social)

admin.site.register(Footer)
admin.site.register(Text)
admin.site.register(Footercont)

admin.site.register(Page)
admin.site.register(Slider)
admin.site.register(Pagenext)
admin.site.register(Projects)
admin.site.register(Example)

admin.site.register(Pictures)
admin.site.register(Short)
admin.site.register(Pageproject)