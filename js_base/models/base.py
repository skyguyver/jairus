from openerp import models, fields

class common_code(models.Model):
    _name = 'js.common_code'
    _description = 'Common Code table'

    name = fields.Char()
    code = fields.Char()
    code_type = fields.Char()
