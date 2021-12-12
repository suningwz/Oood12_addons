# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import exceptions, fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _type_selection_list = [('none', 'NONE'),('rgt', 'RGT'), ('spp', 'SPP'), ('acc', 'ACC'), ('ctl', 'CTL'), ('cons', 'CONS'), ('app', 'APP'), ('cal', 'CAL'), ('fluid', 'FLUID'), ('ser', 'SER')]
    _famille_selection_list = [('none','NONE'),('microbiologie','Microbiologie'),('ia_ocd','IA OCD'),('groupage','GROUPAGE'),('ih','IH'),('hba1c','HBA1C'),('ai','AI'),('cc','CC'),('hemostase','HEMOSTASE'),('cc_ocd','CC OCD'),('biomol','BIOMOL'),('hla','HLA'),('ia&cc_ocd','IA&CC OCD'),('ic','IC'),('oncologie','Oncologie')]
    _temperature_selection_list = [('Ambiant', 'Ambiant'),('2-8', '2-8 °C'), ('-20', '-20 °C'), ('-60', '-60 °C'), ('-80', '-80 °C')]

    product_type = fields.Selection(_type_selection_list, string='Type', default='none', store=True)
    cdt = fields.Integer(string='CDT', store=True)
    temperatur_type = fields.Selection(_temperature_selection_list, string='Temperature', required=True, store=True)

    famille = fields.Selection(_famille_selection_list, string='Famille', default='none', store=True)

    quantity_pi = fields.Integer(string='Quantity PI', store=True)
    tarif_douane = fields.Char(string='Tarif Douanlier', store=True)

    @api.onchange('cdt')
    def _compute_CDT(self):
        if not (self.cdt):
            return
        if self.cdt < 0 or self.cdt > 20000 :
            return {'warning' :{
                'title':"Incorrect Intiger value",
                'message':"La valeur est negative ou superieur a 20 000",
            }}

    @api.onchange('quantity_pi')
    def _compute_quantity_pi(self):
        if not (self.quantity_pi):
            return
        if self.quantity_pi < 0 :
            return {'warning' :{
                'title':"Incorrect Intiger value",
                'message':"La valeur est negative",
            }}

    @api.constrains('cdt', 'quantity_pi')
    def _check_dates(self):
        if self.cdt < 0 or self.quantity_pi < 0 :
            raise ValidationError(_('Error ! La valeur de CDT et/ou Quantite PI sont negatives.'))
