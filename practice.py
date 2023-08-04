from decimal import Decimal


price_ = 140.01

price = Decimal(str(price_)).quantize(Decimal('0.01'))
quantity = Decimal(str(1.233)).quantize(Decimal('0.001'))
cost1 = Decimal(quantity * price).quantize(Decimal('0.01'))

price2 = Decimal(str(10.01)).quantize(Decimal('0.01'))
quantity2 = Decimal(str(1.1)).quantize(Decimal('0.001'))
cost2 = Decimal(quantity2 * price2).quantize(Decimal('0.01'))

total_cost = cost2 + cost1
discount = total_cost * Decimal(str(0.05)).quantize(Decimal('0.01'))
final_discount = Decimal(discount).quantize(Decimal('0.01'))

final = total_cost - final_discount
print(final)
