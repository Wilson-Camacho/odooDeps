# -*- coding: utf-8 -*-
# -*- hola-*-
from odoo import models, fields, api

class lista_tareas(models.Model):

    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'


    avatar = fields.Image("Imagen tarea", max_width=50, max_height = 50)

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    
    fecha = fields.Date()

    @api.depends('prioridad')
    
    def _value_urgente(self):
    
        for record in self:
    
            if record.prioridad > 8:
                record.urgente = True
            else:
                record.urgente = False
