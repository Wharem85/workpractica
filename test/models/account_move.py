# -*- coding: utf-8 -*-

from odoo import models, fields

class AccountMove(models.Model):

	_inherit = "account.move"

	serie = fields.Char(string = "Serie", index = True, copy = False, help = "Serie de la factura")
	numero = fields.Char(string = "Numero", index = True, copy = False, help = "Numero de la factura")
