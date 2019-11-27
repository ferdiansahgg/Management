from odoo import api, fields, models

class Capacity(models.Model):
    _name = "management.capacity"
    
    no = fields.Char("No", require=True, size=10)
    rack = fields.Text("Rack", require=True, size=100)
    used = fields.Text("Used", size=100)
    available = fields.Char("Available", require=True, size=100)