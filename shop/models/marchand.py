# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ShopMarchand(models.Model):
    
    _name = 'shop.marchand'
     

    name = fields.Char(compute="_get_full_name", store=True)
    f_name = fields.Char("Prénom")
    l_name = fields.Char("Nom")
    sexe = fields.Selection([('male','Male'), ('female','Female')])
    
#one2many

    boutique_ids = fields.One2many(comodel_name='shop.boutique', inverse_name='marchand_id')
    
    
    @api.depends('f_name', 'l_name')
    def _get_full_name(self):
        for rec in self:
            if rec.f_name and rec.l_name:
                rec.name = rec.f_name +" "+ rec.l_name