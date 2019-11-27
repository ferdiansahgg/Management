from odoo import api, fields, models

class Subunit(models.Model):
    _name = "management.subunit"
    
    name = fields.Char("Sub Unit", require=True, size=100)
    no_subunit = fields.Integer("No Sub Unit", require=True, size=100)