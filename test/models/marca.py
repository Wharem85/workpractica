 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class Marca(models.Model):
    _inherit = ['format.address.mixin', 'avatar.mixin']
    _description = 'Marca'
    _name = "marca"
    _order = 'name desc, id desc'

    referencia = fields.Char(string='Referencia')
    name = fields.Char(string="Nombre")
    tipo = fields.Char(string="Tipo")
    vehiculo_id = fields.One2many('vehiculo', 'marca_id', string="Vehiculos")
