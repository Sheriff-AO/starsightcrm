import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView
from formtools.wizard.views import SessionWizardView

from .forms import *
from .models import *

# Create your views here.


@login_required
def index(request):
    return render(request, 'audits/index.html')


# @login_required
# def checklistBank(request):
#     if request.method == 'POST':
#         form = CoolingAndPowerInfoForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect('index')

#     else:
#         form = CoolingAndPowerInfoForm(request.POST)

#     context = {
#         'form': form,

#     }
#     return render(request, 'audits/checklist_bank.html', context)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'clients'


@login_required
def clientDetail(request, pk):
    client = Client.objects.get(id=pk)
    sites = Site.objects.filter(client=client)
    total_site = Site.objects.filter(client=client).count()
    context = {
        'client': client,
        'sites': sites,
        'total_site': total_site
    }
    return render(request, 'audits/clientDetail.html', context)


class SiteListView(LoginRequiredMixin, ListView):
    model = Site
    template_name = 'audits/site.html'
    context_object_name = 'sites'
    ordering = ['-date']


class AllVendorListView(ListView):
    model = Vendor
    template_name = 'audits/all_vendor.html'
    context_object_name = 'vendors'
    ordering = ['-user_id']


def vendorList(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors
    }
    return render(request, 'audits/vendor_list.html', context)


@login_required
def createSite(request):
    form = SiteForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('audits:site')

    context = {
        'form': form
    }
    return render(request, 'audits/site_form.html', context)


@login_required
def createClient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('audits:client')

    context = {
        'form': form
    }
    return render(request, 'audits/client_form.html', context)


@login_required
def createVendor(request):
    form = VendorForm()
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Vendor(name=n)
            t.save()

            request.user.vendor.add(t)
            return redirect('audits:vendor')
    else:
        form = VendorForm(request.POST)

    context = {
        'form': form
    }
    return render(request, 'audits/vendor_form.html', context)


@login_required
def vendorDetail(request, pk):
    schedules = Schedule.objects.all()

    instance = Vendor.objects.get(id=pk)

    sites_per_vendor = schedules.filter(vendor=instance)

    context = {
        'vendor': instance,
        'sites_per_vendor': sites_per_vendor,
        'schedules': schedules

    }
    return render(request, 'audits/vendorDetail.html', context)


@login_required
def updateClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('audits:client')

    context = {
        'form': form
    }
    return render(request, 'audits/update_client.html', context)


@login_required
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('audits:client')
    context = {
        'client': client
    }
    return render(request, 'audits/delete_client.html', context)


@login_required
def updateSite(request, pk):
    site = Site.objects.get(id=pk)
    form = SiteForm(instance=site)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('audits:site')

    context = {
        'form': form
    }
    return render(request, 'audits/update_site.html', context)


@login_required
def deleteSite(request, pk):
    site = Site.objects.get(id=pk)
    if request.method == 'POST':
        site.delete()
        return redirect('audits:site')
    context = {
        'site': site
    }
    return render(request, 'audits/delete_site.html', context)


@login_required
def updateVendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    form = VendorForm(instance=vendor)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('audits:vendor')

    context = {
        'form': form
    }
    return render(request, 'audits/update_vendor.html', context)


@login_required
def deleteVendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('audits:vendor')
    context = {
        'vendor': vendor
    }
    return render(request, 'audits/delete_vendor.html', context)


@login_required
def siteSchedule(request):

    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'audits/site_schedule.html', context)


class ChecklistWizardView(SessionWizardView):
    template_name = "audits/temp.html"
    form_list = [
        CustomerInformationForm, CoolingAndPowerInfoForm,  MountingPlaneForm, LightingForm, ApplianceForm, EPowerSourceForm,
        GeneratorForm, CriticalLoadForm, InverterBatteryForm, OperationHourForm, EquipmentRoomForm, BuildingForm,
        RoofInfoForm, StarsightForm, CustomerForm, GeneralCommentForm,
    ]

    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'photos'))
    

    def done(self, form_list, form_dict, **kwargs):
        customer_info = form_dict['0'].save()
        cooling_and_power = form_dict['1'].save()
        mounting_plane = form_dict['2'].save()
        lighting = form_dict['3'].save()
        appliance = form_dict['4'].save()
        e_power_source = form_dict['5'].save()
        generator = form_dict['6'].save()
        critical_load = form_dict['7'].save()
        inverter_battery = form_dict['8'].save()
        operation_hour = form_dict['9'].save()
        equipment_room = form_dict['10'].save()
        building = form_dict['11'].save()
        roof_info = form_dict['12'].save()
        starsight = form_dict['13'].save()
        customer = form_dict['14'].save()
        general_comment = form_dict['15'].save()
        
       # Creating Checklist object
        Checklist.objects.create(
            customer_information=customer_info,
            cooling_and_power_information=cooling_and_power,
            mounting_plane=mounting_plane,
            lighting=lighting,
            appliance=appliance,
            e_power_source=e_power_source,
            generator=generator,
            critical_load=critical_load,
            inverter_battery=inverter_battery,
            operation_hour=operation_hour,
            equipment_room=equipment_room,
            building=building,
            roof_info=roof_info,
            starsight=starsight,
            customer=customer,
            general_comment=general_comment  
            )

        return redirect('audits:checklist')
        


    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())

        except KeyError:
            return super().get(request, *args, **kwargs)
