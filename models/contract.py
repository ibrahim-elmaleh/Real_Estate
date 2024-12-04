from odoo import models, fields, api

class RealEstateContract(models.Model):
    _name = 'real.estate.contract'
    _description = 'Real Estate Contract'

    name = fields.Char(string="Contract Name", required=True)
    property_id = fields.Many2one('real.estate.property', string="Property", required=True)
    tenant_name = fields.Char(string="Tenant Name", required=True)
    rent_amount = fields.Float(string="Rent Amount", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)

    class RealEstateDocument(models.Model):
        _name = 'real.estate.document'
        _description = 'Real Estate Document'
        name = fields.Char(string='Document Name', required=True)
        file = fields.Binary(string='File', required=True)
        property_id = fields.Many2one('real.estate.contract', string='Property', ondelete='cascade')        # New fields for tabs
    sub_project_name = fields.Char(string='Sub Project Name')
    property_details = fields.Text(string='Property Details')
    floor_plan_image1 = fields.Binary("Floor Plan Image 1")
    floor_plan_image2 = fields.Binary("Floor Plan Image 2")
    document_ids = fields.One2many('real.estate.document', 'property_id', string='Documents')
    additional_info = fields.Text(string='Additional Information')
    note = fields.Text(string='Note')


