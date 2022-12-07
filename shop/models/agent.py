# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ShopAgent(models.Model):
    
    _name = 'shop.agent'
     

    f_name = fields.Char("Prénom")
    l_name = fields.Char("Nom")
    sexe = fields.Selection([('male','Male'), ('female','Female')])
    

  
