from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description ="Real Estate"
    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection = [('East','e'), ('West','w'),('North','n'), ('South','s')],
        help = 'Garden orientation'
    )

