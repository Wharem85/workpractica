# -*- coding: utf-8 -*-

from odoo import api, fields, models, Command, _

class Estudiantes(models.Model):
    _inherit = ['format.address.mixin', 'avatar.mixin']
    _name = "estudiantes"
    _description = "Estudiantes models"
    _order = 'name desc, id desc'

    name = fields.Char(string = "Nombre")
    age = fields.Integer(string='Age')
    gender = fields.Selection([
			('male', 'Male'),
			('female', 'Female')
		], string='Gender')
    direccion = fields.Char(string = "Direccion")
    telefono = fields.Char(string = "Telefono")
    padre_familia = fields.Char(string = "Padre de familia")
    pais = fields.Char(string='Pais')
    estado = fields.Selection([
      ('true', 'Activo'),
      ('false', 'No activo')
    ])
    correo = fields.Char(string = "Correo")
