from odoo import api, fields, models

class Unit(models.Model):
    _name = "management.unit"
    
    name = fields.Char("Unit", require=True, size=100)
    no_unit = fields.Integer("No Unit", require=True, size=100)