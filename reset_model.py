# -*- coding: utf-8 -*-
import sys, os
from odoo import models, fields


class ResetButton(models.Model):
    _name = 'reset.button'
    
    def reset_database(self):
        try:
            os.system('sh resetDemo.sh')
        except:
            raise Exception("Reset function failed")






