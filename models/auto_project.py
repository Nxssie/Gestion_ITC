from odoo import models, fields, api
from datetime import timedelta

class Project(models.Model):
  _inherit = 'proyectos.proyectos'

  @api.models
  def create(self, values):
    res = super(Project, self).create(values)
    print(res)

    new1 = self.env['mail_activity'].create({
      'user_id': res.user_id.id, #2
      'res_model_id': res.project_id.alias_model_id.id, #121
      'res_id': res.id, #2
      'date_deadline': fields.Date.today(),
      'res_name': res.name, #0
      'note': "<p>You have a new pending project...</p>",
      'summary': "New project.",
      'activity_pipe_id': 4,
    })
    print(new1)

    return res