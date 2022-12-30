# -*- coding: utf-8 -*-
# by khk
from odoo import fields, models


class HrSalaryRuleInherit(models.Model):
    _inherit = 'hr.salary.rule'

    simulate_ok = fields.Boolean(string='Peut être simulée', default=False,
                                help="Used to check if the salary rule can be used for simulation")