from odoo import models, fields, api
import requests



class Region(models.Model):
    _name = 'region.management'
    _description = 'Region Management'


    # الحقول الحالية
    name = fields.Char(string="Complete Name", required=True)
    parent_id = fields.Many2one('region.management', string="Parent Region", help="Parent region for hierarchy")
    child_ids = fields.One2many('region.management', 'parent_id', string="Sub-regions")
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    project_ids = fields.One2many('project.project', 'region_id', string="Projects")
    latitude = fields.Float(string="Latitude")
    longitude = fields.Float(string="Longitude")

    # الوراثة من res.partner
    address = fields.Char(related='partner_id.street', string="Address", store=True, readonly=False)
    street = fields.Char(related='partner_id.street', string="Street", store=True, readonly=False)
    street2 = fields.Char(related='partner_id.street2', string="Street 2", store=True, readonly=False)
    city = fields.Char(related='partner_id.city', string="City", store=True, readonly=False)
    state_id = fields.Many2one('res.country.state', related='partner_id.state_id', string="State", store=True, readonly=False)
    country_id = fields.Many2one('res.country', related='partner_id.country_id', string="Country", store=True, readonly=False)
    zip = fields.Char(related='partner_id.zip', string="ZIP", store=True, readonly=False)
    ref = fields.Char('Reference')
    # ربط مع res.partner
    partner_id = fields.Many2one('res.partner', string="Partner")

    def compute_coordinates(self):
        for record in self:
            if record.street and record.city and record.state and record.zip_code and record.country:
                address = f"{record.street}, {record.city}, {record.state}, {record.zip_code}, {record.country}"
                url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        record.latitude = float(data[0]['lat'])
                        record.longitude = float(data[0]['lon'])
                    else:
                        record.latitude = 0.0
                        record.longitude = 0.0
                else:
                    record.latitude = 0.0
                    record.longitude = 0.0






class Project(models.Model):
    _inherit = 'project.project'

    region_id = fields.Many2one('region.management', string="Region")


