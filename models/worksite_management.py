from odoo import models, fields, api


class WorksiteManagement(models.Model):
    _name = 'worksite.management'
    _description = 'Worksite Management'

    name = fields.Char(string="Worksite Name", required=True)
    project_type = fields.Selection([
        ('tower', 'Tower'),
        ('villa', 'Villa'),
        ('commercial', 'Commercial (Mall)'),
        ('open_plots', 'Open Plots'),
        ('warehouse', 'Warehouse'),
    ], string="Project Type", required=True, help="Type of the project")

    # الحقول المشتركة
    address = fields.Char(string="Address")
    region_id = fields.Many2one(
        'region.management', string="Region",
        help="Select the region for this project.")
    zip_code = fields.Char(string="ZIP")

    # الحقول الخاصة بـ Tower
    number_of_rooms = fields.Integer(string="Number of Rooms")
    balcony = fields.Boolean(string="Has Balcony")

    # الحقول الخاصة بـ Open Plots
    available_area = fields.Float(string="Available Area (sq.m)")

    @api.onchange('project_type')
    def _onchange_project_type(self):
        """
        تحديث الحقول بناءً على نوع المشروع المختار
        """
        if self.project_type == 'tower':
            self.number_of_rooms = 0
            self.balcony = False
            self.available_area = False
        elif self.project_type == 'open_plots':
            self.number_of_rooms = False
            self.balcony = False
            self.available_area = 0.0
        else:
            self.number_of_rooms = False
            self.balcony = False
            self.available_area = False
