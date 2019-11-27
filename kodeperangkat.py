from odoo import api, fields, models

class Kodeperangkat(models.Model):
    _name = "management.kodeperangkat"
    
    name = fields.Char("No Perangkat", require=True, size=10)
    golperangkat = fields.Char("Golongan Perangkat", require=True, size=100)