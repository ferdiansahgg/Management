from odoo import api, fields, models

class kelompokperangkat(models.Model):
    _name = "management.kelompokperangkat"
    
    name = fields.Char("Kode/Golongan Perangkat", require=True, size=10)
    nokelperangakat = fields.Char("No Kelompok Perangkat", require=True, size=100)
    namakelompok = fields.Char("Nama Kelompok Perangkat", require=True, size=100)