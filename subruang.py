from odoo import api, fields, models

class userdata(models.Model):
    _name = "management.subruang"
    
    name = fields.Char("Sub Ruang", require=True, size=100)
    ruang = fields.Char("Ruang", require=True, size=100)
    no_subruang = fields.Char("No Sub Ruang", require=True, size=100)
    