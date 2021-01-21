from django.db.models import fields
from import_export import resources
from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin


admin.site.register(CoolingAndPowerInfo)
admin.site.register(GeneralComment)
admin.site.register(Client)
admin.site.register(Vendor)
admin.site.register(Schedule)
admin.site.register(CustomerInformation)
admin.site.register(MountingPlane)
admin.site.register(Lighting)
admin.site.register(Appliance)
admin.site.register(EPowerSource)
admin.site.register(Generator)
admin.site.register(CriticalLoad)
admin.site.register(InverterBattery)
admin.site.register(OperationHour)
admin.site.register(EquipmentRoom)
admin.site.register(Building)
admin.site.register(RoofInfo)
admin.site.register(Starsight)
admin.site.register(Customer)


class ChecklistResource(resources.ModelResource):
    def get_export_headers(self):
        print(self.get_export_fields)
        headers = []
        for field in self.get_fields():
            model_fields = self.Meta.model._meta.get_fields()
            header = next((x.verbose_name for x in model_fields if x.name ==
                           field.column_name), field.column_name)
            headers.append(header)
        return headers

    class Meta:
        model = Checklist
        fields = ('cooling_and_power_information__location',
                  'cooling_and_power_information__existing_qty_standing_unit')


@admin.register(Checklist)
class ViewAdmin(ImportExportModelAdmin):
    resource_class = ChecklistResource


@admin.register(Site)
class ImportSite(ImportExportModelAdmin):
    pass
