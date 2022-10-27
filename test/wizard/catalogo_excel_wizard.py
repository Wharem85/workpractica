# -*- coding: utf-8 -*-

from itertools import product
import xlrd
import binascii
import tempfile
import io
from odoo import api, fields, models, _
import logging
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo.fields import Datetime, Date
from datetime import datetime
from odoo import Command


_logger = logging.getLogger(__name__)


try:
    import xlwt
except ImportError:
    _logger.debug('Cannot `import xlwt`.')
try:
    import cStringIO
except ImportError:
    _logger.debug('Cannot `import cStringIO`.')
try:
    import base64
except ImportError:
    _logger.debug('Cannot `import base64`.')


class ImportarCatalogosExcel(models.TransientModel):

    _name = "importar.catalogos.excel.wizard"
    _description = "Importar Archivos de Excel"

    archivo = fields.Binary(string="Archivo (XLS)")
    tipo_plantilla = fields.Selection([
        ('p1', 'Cargar Catalogo de vehiculos'),
        ('p2', 'Cargar Catalogo de marca'),
    ], required=True, default='p1')

    def cargar_catalogo_excel(self):
        if self.tipo_plantilla == 'p1':
            self._cargar_catalgo_vehiculo()
        if self.tipo_plantilla == 'p2':
            self._cargar_catalgo_marca()

    def _cargar_catalgo_vehiculo(self):
        fp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
        fp.write(binascii.a2b_base64(self.archivo))
        fp.seek(0)
        values = []
        workbook = xlrd.open_workbook(fp.name)
        sheet = workbook.sheet_by_index(0)

        i = 0

        for row_no in range(sheet.nrows):
            i = i +1
            if row_no <= 0:
                fields = map(lambda row: row.value.encode(
                    'utf-8'), sheet.row(row_no))
            else:
                line = list(map(lambda row: isinstance(row.value, bytes) and row.value.encode(
                    'utf-8') or str(row.value), sheet.row(row_no)))
                datos = {
                    'referencia': line[0],
                    'name': line[1],
                    'recurso': line[2],
                    'placa': line[3],
                }

                name = 'vehiculo_' + line[0]

                buscar_vehiculo = self.env['ir.model.data'].search(
                    [('name', '=', name)])

                if not buscar_vehiculo:
                    contacto = self.env['vehiculo'].create(datos)
                    self.env['ir.model.data'].create({
                        'name': name,
                        'model': 'vehiculo',
                        'module': '__export__',
                        'res_id': contacto.id,
                    })

        return True

    def _cargar_catalgo_marca(self):
        fp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
        fp.write(binascii.a2b_base64(self.archivo))
        fp.seek(0)
        values = []
        workbook = xlrd.open_workbook(fp.name)
        sheet = workbook.sheet_by_index(0)

        i = 0

        for row_no in range(sheet.nrows):
            i = i +1
            if row_no <= 0:
                fields = map(lambda row: row.value.encode(
                    'utf-8'), sheet.row(row_no))
            else:
                line = list(map(lambda row: isinstance(row.value, bytes) and row.value.encode(
                    'utf-8') or str(row.value), sheet.row(row_no)))
                datos = {
                    'referencia': line[0],
                    'name': line[1],
                    'tipo': line[2],
                }

                name = 'marca_' + line[0]

                buscar_marca = self.env['ir.model.data'].search(
                    [('name', '=', name)])

                if not buscar_marca:
                    contacto = self.env['marca'].create(datos)
                    self.env['ir.model.data'].create({
                        'name': name,
                        'model': 'marca',
                        'module': '__export__',
                        'res_id': contacto.id,
                    })

        return True
