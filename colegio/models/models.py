from odoo import models, fields, api


class colegio(models.Model):
    _name = 'colegio.models'
    _description = 'colegio models'

    name = fields.Char(string='Nombre')
    age = fields.Integer(string='Edad')
    gender = fields.Selection([
			('male', 'Hombre'),
			('female', 'Mujer')
		], string='Genero')
    direccion = fields.Char(string='Direccion')
    telefono = fields.Char(string='Telefono')
    padre_familiar = fields.Char(string='Padres de familia')
    # pais = fields.Char(string='Pais')
    # estado = fields.Selection([
    #   ('true', 'Activo'),
    #   ('false', 'No activo')
    # ])
