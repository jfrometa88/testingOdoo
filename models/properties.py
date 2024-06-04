from odoo import fields,models

class Property(models.Model):
    _name="estate.property"
    _description="Estate Property"
    name=fields.Char(string="Name",required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="PostCode")
    date_availability = fields.Date(string="Available from")
    expected_price = fields.Float(string="Expected Price")
    best_offer= fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms=fields.Integer(string="Bedrooms")
    living_area=fields.Float(string="Living Area")
    garage=fields.Boolean(string="Garage",default=False)
    garden=fields.Boolean(string="Garden",default=False)
    garden_orientation=fields.Selection([("north","North"),
                                        ("east","East"),
                                        ("south","South"),
                                        ("west","West")],default="north")
