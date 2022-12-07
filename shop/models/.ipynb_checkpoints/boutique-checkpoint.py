# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ShopBoutique(models.Model):
    
    _name = 'shop.boutique'
    
    name = fields.Char("Nom")
    lieu = fields.Char("Lieu")
    
    marchand_id = fields.Many2one(comodel_name='shop.marchand')
    