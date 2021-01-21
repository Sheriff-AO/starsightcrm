from django.forms import forms
from django.contrib.auth.models import User
from .models import *
from django import forms


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'


class CoolingAndPowerInfoForm(forms.ModelForm):

    class Meta:
        model = CoolingAndPowerInfo
        fields = '__all__'


class CustomerInformationForm(forms.ModelForm):
    class Meta:
        model = CustomerInformation
        fields = '__all__'


class MountingPlaneForm(forms.ModelForm):
    class Meta:
        model = MountingPlane
        fields = '__all__'


class LightingForm(forms.ModelForm):
    class Meta:
        model = Lighting
        fields = '__all__'


class ApplianceForm(forms.ModelForm):
    class Meta:
        model = Appliance
        fields = '__all__'


class EPowerSourceForm(forms.ModelForm):
    class Meta:
        model = EPowerSource
        fields = '__all__'


class GeneratorForm(forms.ModelForm):
    class Meta:
        model = Generator
        fields = '__all__'


class CriticalLoadForm(forms.ModelForm):
    class Meta:
        model = CriticalLoad
        fields = '__all__'


class InverterBatteryForm(forms.ModelForm):
    class Meta:
        model = InverterBattery
        fields = '__all__'


class OperationHourForm(forms.ModelForm):
    class Meta:
        model = OperationHour
        fields = '__all__'


class EquipmentRoomForm(forms.ModelForm):
    class Meta:
        model = EquipmentRoom
        fields = '__all__'


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'


class RoofInfoForm(forms.ModelForm):
    class Meta:
        model = RoofInfo
        fields = '__all__'


class StarsightForm(forms.ModelForm):
    class Meta:
        model = Starsight
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class GeneralComment(forms.ModelForm):
    class Meta:
        model = GeneralComment
        fields = '__all__'
