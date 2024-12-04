from odoo import models, fields

class RealEstateProject(models.Model):
    _name = 'real.estate.project'
    _description = 'Real Estate Project'

    name = fields.Char(string="Project Name", required=True)
    region_id = fields.Many2one(
        'region.management', string="Region",
        help="Select the region for this project.")
    project_type = fields.Selection([('tower', 'Tower'),('villa', 'Villa'),('commercial', 'Commercial (Mall)'),('warehouse', 'Warehouse'), ('plots', 'Open Plots')], string="Project Type")
    properties = fields.One2many('real.estate.property', 'project_id', string="Properties")
    worksite = fields.Many2one(
        'worksite.management', string="Worksite",
        help="Select the region for this project.")
