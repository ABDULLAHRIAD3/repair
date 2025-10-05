from odoo import models ,fields

class SparePart(models.Model):
    _name = 'spare.part'
    name = fields.Char(string="Spare Part")