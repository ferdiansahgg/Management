from odoo import api, fields, models

class userdata(models.Model):
    _name = "management.ruang"
    
    name = fields.Char("Ruang", require=True, size=100)
    lokasi = fields.Char("Lokasi", require=True, size=100)
    no_ruang = fields.Char("No Ruang", require=True, size=100)
    