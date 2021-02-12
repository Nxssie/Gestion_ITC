# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proyectos_proyectos(models.Model):
  _name = 'proyectos.proyectos'

  name = fields.Integer(string="ID proyecto")
  language = fields.Char(string="Lenguaje")
  date = fields.Date(string="Fecha")
  description = fields.Char(string="Usuario que atiende el proyecto")

class proyectos_language(models.Model):
  _name = 'proyectos.language'

  name = fields.Char(string="Nombre")
  framework = fields.Char(string="Framework")
  