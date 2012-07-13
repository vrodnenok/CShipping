# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Vport(models.Model):
    voyages_id = models.IntegerField(null=True, blank=True)
    port = models.CharField(max_length=150, blank=True)
    turn = models.IntegerField(null=True, blank=True)
    ops_type = models.CharField(max_length=45, blank=True)
    agent = models.CharField(max_length=150, blank=True)
    ldrate = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    est_da = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    comment = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'vport'

class Expense(models.Model):
    voyages_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    kind = models.CharField(max_length=45, blank=True)
    location = models.CharField(max_length=150, blank=True)
    amount = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    comment = models.CharField(max_length=150, blank=True)
    balance = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    invoice_date = models.DateTimeField(null=True, blank=True)
    docs_received = models.DateTimeField(null=True, blank=True)
    when_balance_paid = models.DateTimeField(null=True, blank=True)
    benef_details = models.CharField(max_length=150, blank=True)
    docs_archive = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'expense'

class Income(models.Model):
    voyages_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    kind = models.CharField(max_length=45, blank=True)
    location = models.CharField(max_length=150, blank=True)
    amount = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    comment = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'income'


class Bunker(models.Model): 
    voyages_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=150, blank=True)
    kind = models.CharField(max_length=45, blank=True)
    supplied = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    price = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    barging = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    supplier = models.CharField(max_length=150, blank=True)
    comment = models.CharField(max_length=150, blank=True)
    balance = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    invoice_date = models.DateTimeField(null=True, blank=True)
    docs_received = models.DateTimeField(null=True, blank=True)
    when_balance_paid = models.DateTimeField(null=True, blank=True)
    benef_details = models.CharField(max_length=150, blank=True)
    docs_archive = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'bunker'

class Operation(models.Model):
    voyages_id = models.IntegerField(null=True, blank=True)
    vessels_id = models.IntegerField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    ops_type = models.CharField(max_length=45, blank=True)
    location = models.CharField(max_length=150, blank=True)
    coords = models.CharField(max_length=60, blank=True)
    bunk_rob = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    lo_rob = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    fw_rob = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    mileage = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    transit = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    delays = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    reason = models.CharField(max_length=60, blank=True)
    prospects = models.CharField(max_length=150, blank=True)
    weather_comm = models.CharField(max_length=150, blank=True)
    comment = models.TextField(blank=True)
    due_to_weather = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    due_to_strait = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    due_to_weekend = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    due_to_technical = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    due_to_other = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    delay_comm = models.TextField(blank=True)
    class Meta:
        db_table = u'operation'

class Port(models.Model):
    fport = models.CharField(max_length=75, blank=True)
    tport = models.CharField(max_length=75, blank=True)
    region = models.CharField(max_length=21, blank=True)
    distance = models.DecimalField(null=True, max_digits=11, decimal_places=0, blank=True)
    class Meta:
        db_table = u'port'

class Vessel(models.Model):
    vsl_name = models.CharField(max_length=75)
    dwt = models.IntegerField(null=True, blank=True)
    dwcc = models.IntegerField(null=True, blank=True)
    grt = models.IntegerField(null=True, blank=True)
    nrt = models.IntegerField(null=True, blank=True)
    volume = models.IntegerField(null=True, blank=True)
    loa = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    beam = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    dm = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    draft = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    built = models.IntegerField(null=True, blank=True)
    speed_ballast = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    speed_loaded = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    lo1_underway = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    lo2_underway = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    lo3_underway = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    fuel1_underway = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    fuel2_underway = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    fuel3_underway = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    lo1_in_port = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    lo2_in_port = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    lo3_in_port = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    fuel1_in_port = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    fuel2_in_port = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    fuel3_in_port = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    fw_cons = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    salary = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    pandi = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    nav_class = models.IntegerField(null=True, blank=True)
    office_exp_share = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    provisions = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    class Meta:
        db_table = u'vessel'

class Voyage(models.Model):
    vessels_id = models.IntegerField()
    voy_number = models.CharField(max_length=24)
    performer = models.CharField(max_length=81, blank=True)
    charterers = models.TextField(blank=True)
    cargo_type = models.CharField(max_length=90, blank=True)
    first_port = models.CharField(max_length=90, blank=True)
    last_port = models.CharField(max_length=90, blank=True)
    voyage_start = models.DateTimeField(null=True, blank=True)
    est_voyage_compl = models.DateTimeField(null=True, blank=True)
    frt_rate = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    frt_flag = models.IntegerField(null=True, blank=True)
    est_frt = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_cargo_qty = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_cargo_qty = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_mileage = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_mileage = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_fuel_cons = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_fuel_cons = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_lo_cons = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_lo_cons = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_fuel_cost = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_fuel_cost = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_lo_cost = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_lo_cost = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_go_rob = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_go_price = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_go_rob = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_go_price = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_lo_rob = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_lo_price = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_fw_rob = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    act_lo_rob = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_lo_price = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_salary = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_salary = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_fw_cons = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_fw_cons = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_fw_cost = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_fw_cost = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    fw_price = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_pni_exp = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_pni_exp = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    est_office_exp = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_office_exp = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    act_speed = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    inv_date = models.DateTimeField(null=True, blank=True)
    cp_date = models.DateTimeField(null=True, blank=True)
    is_frt_rcvd = models.BooleanField(blank=True)
    est_length = models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)
    load_rate = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    disch_rate = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    ets_ballast_leg = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    is_inv_issued = models.BooleanField(blank=True)
    est_days_in_port = models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)
    act_days_in_port = models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)
    est_days_in_ballast = models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)
    act_days_in_ballast = models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)
    est_days_underway = models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)
    act_days_underway = models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)
    compl_flag = models.BooleanField(blank=True)
    class Meta:
        db_table = u'voyage'
