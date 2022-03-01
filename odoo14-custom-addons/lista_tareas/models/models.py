# -*- coding: utf-8 -*-
# -*- hola-*-
from email.policy import default
from odoo import models, fields, api

class lista_tareas(models.Model):

    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'


    avatar = fields.Image("Imagen tarea", max_width=50, max_height = 50)
    

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    #Nuevo Campos.
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
    estado = fields.Selection(
        [('no', 'Sin hacer'),('si','Hecho')], 'Estado', default = "no")
    fecha = fields.Date()

    @api.depends('prioridad')
    
    def _value_urgente(self):
    
        for record in self:
    
            if record.prioridad > 8:
                record.urgente = True
            else:
                record.urgente = False
