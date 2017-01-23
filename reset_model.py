# -*- coding: utf-8 -*-
import sys, os
from openerp import models, fields
class ResetButton(models.Model):
    _name = 'reset.button'
    def reset_database(self):
        try:
            os.system('su - postgres  -c "sh resetDemo.sh"')
        except:
            raise Exception("Reset function failed")






