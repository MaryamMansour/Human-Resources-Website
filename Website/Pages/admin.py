from django.contrib import admin
from .models import Employee
admin.site.register(Employee)
from .models import Vacation
admin.site.register(Vacation)
# Register your models here.
from .models import Training
from .models import OfficialHoliday
from .models import importantMeeting
admin.site.register(Training)
admin.site.register(OfficialHoliday)
admin.site.register(importantMeeting)

