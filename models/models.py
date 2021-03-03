# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proyectos_proyectos(models.Model):
  _name = 'proyectos.proyectos'
  _inherit = ['mail.thread', 'mail.activity.mixin']

  project_id = fields.Integer(string="ID Proyecto", default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
  description = fields.Char(string="Descripción")
  area = fields.Many2one("proyectos.areas", string="Área", required=True, ondelete="cascade")
  date = fields.Date(string="Fecha")
  user_id = fields.Many2one('res.users',
        string='Asignado a',
        default=lambda self: self.env.uid,
        index=True, track_visibility='always')

class proyectos_areas(models.Model):
  _name = 'proyectos.areas'

  name = fields.Char(string="Área")
  proyectos = fields.One2many("proyectos.proyectos", "area", string="Proyectos")