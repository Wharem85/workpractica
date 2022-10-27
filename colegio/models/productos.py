# -*- coding: utf-8 -*-

from odoo import fields, models

class productos(models.Model):
  _inherit = 'product.template'

  producto_venta_publico = fields.Float(string="Precios de Venta: PUBLICO")
  producto_venta_campana = fields.Float(string="Precios de Venta: CAMPAÑA")
  producto_venta_ofertas = fields.Float(string="Precios de Venta: LISTA DE OFERTAS")
  producto_venta_empleados = fields.Float(string="Precios de Venta: EMPLEADOS")
