# -*- coding: utf-8 -*-

from odoo import api, models, fields


class List(models.Model):
    _name = 'todo.list'
    _description = 'todo.list'

    list_name = fields.Text(string="Tarefa")
    partner_id = fields.Many2one('res.partner', string='Parceiro', required=True, ondelete='cascade', default=lambda self: self.env.uid, help="Parceiro da tarefa")

    

