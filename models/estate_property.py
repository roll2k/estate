from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description ="Real Estate"
    name = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection =[('e', 'East'), ('w', 'West'), ('n', 'North'), ('s', 'South')],
        help = 'Garden orientation'
    )


