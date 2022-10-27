# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vehiculo(models.Model):
    _inherit = ['format.address.mixin', 'avatar.mixin']
    _description = 'Vehiculo'
    _name = "vehiculo"
    _order = 'name desc, id desc'

    referencia = fields.Char(string='Referencia')
    name = fields.Char(string="Nombre")
    recurso = fields.Selection([
        ('electrico', 'Electrico'),
        ('diesel', 'Diesel'),
        ('otro', 'Otro')
    ] ,string="Recurso")
    placa = fields.Char(string='Placa')
    marca_id = fields.Many2one('marca', string='Marca')
