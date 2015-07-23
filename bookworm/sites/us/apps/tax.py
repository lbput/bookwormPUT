from decimal import Decimal as D

def apply_to(submission):
    """
    Calculate and apply taxes to a submission
    """

    shipping_address = submission['shipping_address']
    rate = D('0.05')
	
    for line in submission['basket'].all_lines():
        line_tax = calculate_tax(line.line_price_excl_tax_incl_discounts, rate)
        unit_tax = (line_tax / line.quantity).quantize(D('0.01'))
        line.purchase_info.price.tax = unit_tax

    shipping_charge = submission['shipping_charge']



def calculate_tax(price, rate):
    tax = price * rate
    return tax.quantize(D('0.01'))
