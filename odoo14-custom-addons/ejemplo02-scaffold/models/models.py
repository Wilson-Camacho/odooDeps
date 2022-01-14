# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ejemplo02-scaffold(models.Model):
#     _name = 'ejemplo02-scaffold.ejemplo02-scaffold'
#     _description = 'ejemplo02-scaffold.ejemplo02-scaffold'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
