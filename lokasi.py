from odoo import api, fields, models

class userdata(models.Model):
    _name = "management.lokasi"
    
    name = fields.Char("Lokasi", require=True, size=100)
    no_lokasi = fields.Char("No Lokasi", require=True, size=100)
    