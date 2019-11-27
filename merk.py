from odoo import api, fields, models

class userdata(models.Model):
    _name = "management.merk"
    
    name = fields.Char("Merk", require=True, size=100)
    