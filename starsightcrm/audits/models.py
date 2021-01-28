
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.reverse_related import ManyToOneRel
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.


class Client(models.Model):
    CATEGORY = (
        ('Banking & SMEs', 'Banking & SMEs'),
        ('Commercial & Industries', 'Commercial & Industries'),
    )
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    name = models.CharField(max_length=200, null=True)
    rep_name = models.CharField(max_length=200, null=True)
    designation = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, null=True)
    num_of_site = models.IntegerField(null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


class Vendor(models.Model):
    user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="vendor")
    name = models.CharField(max_length=100, null=True)
    rep_name = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=16, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return str(self.name) if (self.name) else ""


class Site(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50, null=True)
    address = models.TextField(max_length=200, null=True)
    state = models.CharField(max_length=20, null=True)
    region = models.CharField(max_length=4, null=True)
    contact_person = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    contact_num = models.CharField(max_length=16, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.client} - {self.branch}'


class Schedule(models.Model):
    STATUS = (
        ('SfA', 'Scheduled for Audit'),
        ('SfDL', 'Scheduled for Data-logging'),
        ('SfA&DL', 'Scheduled for Audit & Data-logging'),
        ('PS', 'Pending Schedule'),
        ('A', 'Audited'),
        ('DL', 'Data-logged'),
        ('A&DL', 'Audited & Data-logged'),
    )
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)
    sites = models.ManyToManyField(Site)
    date_assigned = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    report_received = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vendor}"


class CoolingAndPowerInfo(models.Model):
    location = models.TextField(_("Location"))
    existing_qty_split_unit = models.CharField(
        _("Existing Split Unit"), max_length=50)
    existing_qty_standing_unit = models.CharField(
        _("Existing Standing Unit"), max_length=50)
    condition_qty_working = models.CharField(
        _("Quantity Working"), max_length=50)
    condition_qty_faulty = models.CharField(
        _("Quantity Faulty"), max_length=50)
    required_qty_split_unit = models.IntegerField(_("Required Split Unit"))
    required_qty_standing_unit = models.IntegerField(
        _("Required Standing Unit"))

    class Meta:
        verbose_name = 'CoolingAndPowerInfo'
        verbose_name_plural = 'CoolingAndPowerInfos'

    def __str__(self):
        return self.location


class CustomerInformation(models.Model):
    client = models.CharField(max_length=100, null=True, blank=True)
    site_full_address = models.CharField(max_length=120, null=True, blank=True)
    gps_coordinate = models.CharField(max_length=18, null=True, blank=True)
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=18, null=True, blank=True)
    date = models.DateTimeField()


class MountingPlane(models.Model):
    rooftop = models.CharField(max_length=20, null=True, blank=True)
    ground_mounted = models.CharField(max_length=20, null=True, blank=True)
    rooftop_ground_mounted = models.CharField(
        max_length=20, null=True, blank=True)


class Lighting(models.Model):
    florescent = models.CharField(max_length=20, null=True, blank=True)
    LED = models.CharField(max_length=20, null=True, blank=True)
    halogen = models.CharField(max_length=20, null=True, blank=True)
    energy_saver = models.CharField(max_length=20, null=True, blank=True)
    panel_light = models.CharField(max_length=20, null=True, blank=True)
    others = models.CharField(max_length=20, null=True, blank=True)


class Appliance(models.Model):
    desktop = models.IntegerField()
    laptop = models.IntegerField()
    printer = models.IntegerField(null=True, blank=True)
    counting_machine = models.IntegerField(null=True, blank=True)
    scanner = models.IntegerField(null=True, blank=True)
    atms = models.IntegerField(null=True, blank=True)
    tv = models.IntegerField(null=True, blank=True)
    water_dispenser = models.IntegerField(null=True, blank=True)
    exchange_rate_board = models.IntegerField(null=True, blank=True)
    signage_light = models.IntegerField(null=True, blank=True)
    water_pump = models.IntegerField(null=True, blank=True)
    fan = models.IntegerField(null=True, blank=True)
    microwave = models.IntegerField(null=True, blank=True)
    card_printer = models.IntegerField(null=True, blank=True)
    time_stamping_machine = models.IntegerField(null=True, blank=True)
    shredder = models.IntegerField(null=True, blank=True)
    sorting_machine = models.IntegerField(null=True, blank=True)
    fridge = models.IntegerField(null=True, blank=True)
    mantrap_door = models.IntegerField(null=True, blank=True)
    hand_dryer = models.IntegerField(null=True, blank=True)


class EPowerSource(models.Model):
    connects_to_grid = models.BooleanField(null=True)
    connects_to_solar = models.BooleanField(null=True)
    connects_to_generator = models.BooleanField(null=True)
    has_dedicated_transformer = models.BooleanField(null=True)


class Generator(models.Model):
    genset_1 = models.CharField(max_length=20, null=True, blank=True)
    genset_2 = models.CharField(max_length=20, null=True, blank=True)
    genset_3 = models.CharField(max_length=20, null=True, blank=True)
    transformer = models.CharField(max_length=20, null=True, blank=True)


class CriticalLoad(models.Model):
    item1 = models.CharField(max_length=50, null=True, blank=True)
    item2 = models.CharField(max_length=50, null=True, blank=True)
    item3 = models.CharField(max_length=50, null=True, blank=True)
    item4 = models.CharField(max_length=50, null=True, blank=True)
    item5 = models.CharField(max_length=50, null=True, blank=True)
    item6 = models.CharField(max_length=50, null=True, blank=True)
    item7 = models.CharField(max_length=50, null=True, blank=True)


class InverterBattery(models.Model):
    inverter_1 = models.CharField(max_length=20, null=True, blank=True)
    inverter_2 = models.CharField(max_length=20, null=True, blank=True)
    inverter_3 = models.CharField(max_length=20, null=True, blank=True)
    ups_1 = models.CharField(max_length=20, null=True, blank=True)
    ups_2 = models.CharField(max_length=20, null=True, blank=True)
    ups_3 = models.CharField(max_length=20, null=True, blank=True)
    stabilizer_1 = models.CharField(max_length=20, null=True, blank=True)
    stabilizer_2 = models.CharField(max_length=20, null=True, blank=True)
    battery_bank_1 = models.CharField(max_length=20, null=True, blank=True)
    battery_bank_2 = models.CharField(max_length=20, null=True, blank=True)
    battery_bank_3 = models.CharField(max_length=20, null=True, blank=True)
    battery_bank_4 = models.CharField(max_length=20, null=True, blank=True)


class OperationHour(models.Model):
    opening_time = models.CharField(max_length=6, null=True, blank=True)
    closing_time = models.CharField(max_length=6, null=True, blank=True)
    monday_to_friday = models.BooleanField(default=False)
    monday_to_saturday = models.BooleanField(default=False)
    monday_to_sunday = models.BooleanField(default=False)


class EquipmentRoom(models.Model):
    available = models.BooleanField(default=False)
    on_what_floor = models.CharField(max_length=18, null=True, blank=True)
    dimension = models.CharField(max_length=10, null=True, blank=True)
    distance_to_generator = models.CharField(
        max_length=10, null=True, blank=True)


class Building(models.Model):
    bungalow = models.BooleanField(default=False)
    one_storey = models.BooleanField(default=False)
    two_storey = models.BooleanField(default=False)
    three_storey = models.BooleanField(default=False)
    others = models.BooleanField(default=False)
    building_picture = models.ImageField(
        default='default1.jpg',  upload_to='building_pics/')
    roof_picture = models.ImageField(
        default='default2.jpg', upload_to='roof_pics/')


class RoofInfo(models.Model):
    roof_dimension = models.CharField(max_length=20, null=True, blank=True)
    total_area = models.IntegerField()
    number_of_panels = models.IntegerField()
    roof_type = models.CharField(max_length=20, null=True, blank=True)
    roofing_sheet_material = models.CharField(
        max_length=20, null=True, blank=True)
    roofing_sheet_thickness = models.CharField(
        max_length=20, null=True, blank=True)
    roofing_sheet_lapping = models.CharField(
        max_length=20, null=True, blank=True)
    roofing_truss = models.CharField(max_length=20, null=True, blank=True)
    general_comment = models.TextField(max_length=300, null=True, blank=True)


class Starsight(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)


class Customer(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)


class GeneralComment(models.Model):
    comment = models.TextField(null=True, blank=True)


class Checklist(models.Model):
    customer_information = models.OneToOneField("audits.CustomerInformation", verbose_name=_(
        "Customer Information"), on_delete=models.CASCADE)
    cooling_and_power_information = models.OneToOneField("audits.CoolingAndPowerInfo", verbose_name=_(
        "Cooling and Power Information"), on_delete=models.CASCADE)
    mounting_plane = models.OneToOneField("audits.MountingPlane", verbose_name=_(
        "Available Mounting Planes"), on_delete=models.CASCADE)
    lighting = models.OneToOneField("audits.Lighting", verbose_name=_(
        "Lightings"), on_delete=models.CASCADE)
    appliance = models.OneToOneField("audits.Appliance", verbose_name=_(
        "Appliances"), on_delete=models.CASCADE)
    e_power_source = models.OneToOneField("audits.EPowerSource", verbose_name=_(
        "Existing Power Sources"), on_delete=models.CASCADE)
    generator = models.OneToOneField("audits.Generator", verbose_name=_(
        "Generator & Transformer Details"), on_delete=models.CASCADE)
    critical_load = models.OneToOneField("audits.CriticalLoad", verbose_name=_(
        "Critical Loads Details"), on_delete=models.CASCADE)
    inverter_battery = models.OneToOneField("audits.InverterBattery", verbose_name=_(
        "Inverter/Battery/UPS Details"), on_delete=models.CASCADE)
    operation_hour = models.OneToOneField("audits.OperationHour", verbose_name=_(
        "Operation Hour"), on_delete=models.CASCADE)
    equipment_room = models.OneToOneField("audits.EquipmentRoom", verbose_name=_(
        "Equipment Room Details"), on_delete=models.CASCADE)
    building = models.OneToOneField("audits.Building", verbose_name=_(
        "Description of the Building with pictures"), on_delete=models.CASCADE)
    roof_info = models.OneToOneField("audits.RoofInfo", verbose_name=_(
        "Roof Information"), on_delete=models.CASCADE)
    starsight = models.OneToOneField("audits.Starsight", verbose_name=_(
        "Starsight Representative"), on_delete=models.CASCADE)
    customer = models.OneToOneField("audits.Customer", verbose_name=_(
        "Customer Representative"), on_delete=models.CASCADE)
    general_comment = models.OneToOneField("audits.GeneralComment", verbose_name=_(
        "General Comment"), on_delete=models.CASCADE)
