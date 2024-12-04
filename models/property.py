from odoo import models, fields, api
from odoo.exceptions import UserError

class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string="Property Name", required=True)
    price = fields.Float(string="Price (Per SFT)")
    tenant_id = fields.Many2one('res.partner', string='Tenant', help='The tenant renting this property.')
    project_id = fields.Many2one('real.estate.project', string="Project")
    availability = fields.Selection([('available', 'Available'), ('sold', 'Sold')], string="Status",
                                    default='available')


    def action_create_rental_contract(self):
        """ Create a rental contract for this property """
        contract_vals = {
            'name': f'Rental Contract for {self.name}',
            'property_id': self.id,
            'tenant_name': self.tenant_id or 'Default Tenant',
            'rent_amount': self.price or 0.0,
            'start_date': fields.Date.today(),
            'end_date': fields.Date.add(fields.Date.today(), months=12),  # افتراض مدة العقد سنة واحدة
        }
        contract = self.env['real.estate.contract'].create(contract_vals)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Rental Contract',
            'res_model': 'real.estate.contract',
            'view_mode': 'form',
            'res_id': contract.id,
            'target': 'new',
        }



    def action_create_invoice(self):
        """ Generate invoice for the property """
        # تحقق من وجود السعر
        if not self.price:
            raise UserError("Please set a valid price for this property before creating an invoice.")

        # تعريف قيم الفاتورة
        invoice_vals = {
            'move_type': 'out_invoice',  # فاتورة مبيعات
            'partner_id': self.tenant_id.id if self.tenant_id else self.env.user.partner_id.id,  # العميل
            'invoice_line_ids': [(0, 0, {
                'name': f'Property Rent: {self.name}',
                'quantity': 1,
                'price_unit': self.price,
            })],
        }

        # إنشاء الفاتورة
        invoice = self.env['account.move'].create(invoice_vals)

        # فتح الفاتورة في النموذج
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoice',
            'res_model': 'account.move',
            'view_mode': 'form',
            'res_id': invoice.id,
            'target': 'current',
        }

