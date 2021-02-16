# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proyectos_proyectos(models.Model):
  _name = 'proyectos.proyectos'

  name = fields.Integer(string="ID proyecto")
  area = fields.Many2one("proyectos.areas", string="Area", required=True, ondelete="cascade")
  date = fields.Date(string="Fecha")
  description = fields.Char(string="Usuario que atiende el proyecto")

class proyectos_areas(models.Model):
  _name = 'proyectos.areas'

  name = fields.Char(string="Área")
  proyectos = fields.One2many("proyectos.proyectos", "proyecto", string="Proyectos")
  