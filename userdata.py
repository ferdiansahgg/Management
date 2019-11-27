from odoo import api, fields, models

class userdata(models.Model):
    _name = "management.userdata"
    
    name = fields.Char("Username", require=True, size=100)
    identitas = fields.Char("Identitas", size=100)
    namalengkap = fields.Char("Nama Lengkap", require=True, size=100)
    level = fields.Char("Level", size=50)
    blokir = fields.Char("Blokir", size=100)
    pemandu = fields.Char("Pemandu", size=100)
    pengelola = fields.Char("Pengelola", size=100)
    tempadmin = fields.Char("Temp Admin", size=100)