from odoo import api, fields, models

class Asset(models.Model):
    _name = "management.assetnondc"
    
    no = fields.Char("No", require=True, size=10)
    pemilik = fields.Text("SKPD/UKPD/Pemilik", require=True, size=100)
    ruang = fields.Text("Ruang/Posisi", size=100)
    no_reg = fields.Char("No.Reg/SN/IP", require=True, size=100)
    model = fields.Text("Merk/Model/Tipe", size=50)
    spesifikasi = fields.Text("Spesifikasi", size=100)
    fungsi = fields.Text("Fungsi", size=50)
    visit = fields.Char("Visit", size=10)
    note = fields.Text("Note", size=100)
    maintenance_id = fields.One2many(comodel_name="management.maintenance",
    	inverse_name="assetnondc_id",
    	string="Maintenance", required=False)
    image_small = fields.Binary(string="Image Small",)