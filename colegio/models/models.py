from odoo import models, fields, api


class colegio(models.Model):
    _name = 'colegio.models'
    _description = 'colegio models'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
			('male', 'Male'),
			('female', 'Female')
		], string='Gender')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
