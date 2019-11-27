from odoo import api, fields, models

class Agenda(models.Model):
    _name = "management.agenda"
    
    no = fields.Char("No", require=True, size=10)
    tema = fields.Text("Tema", require=True, size=100)
    tgl_mulai = fields.Date("Tgl.Mulai", size=100)
    tgl_selesai = fields.Date("Tgl.Selesai", require=True, size=100)