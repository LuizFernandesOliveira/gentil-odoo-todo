# -*- coding: utf-8 -*-
{
    'name': "todo",
    'summary': "Todo List for your work",
    'author': "Luiz Fernandes de Oliveira",
    'website': "https://github.com/LuizFernandesOliveira/gentil_odoo_todo",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/todo_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
