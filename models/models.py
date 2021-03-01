# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proyectos_proyectos(models.Model):
  _name = 'proyectos.proyectos'
  _inherit = ['mail.thread', 'mail.activity.mixin']

  name = fields.Integer(string="ID proyecto")
  description = fields.Char(string="Descripción")
  area = fields.Many2one("proyectos.areas", string="Area", required=True, ondelete="cascade")
  date = fields.Date(string="Fecha")
  employee = fields.Many2one("hr.employee", string="Empleado que atiende el proyecto", required=True, ondelete="cascade")

class proyectos_areas(models.Model):
  _name = 'proyectos.areas'

  name = fields.Char(string="Área")
  proyectos = fields.One2many("proyectos.proyectos", "area", string="Proyectos")