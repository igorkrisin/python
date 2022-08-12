number_pizzas = eval(input('Сколько пицц Вы хотите? '))
cost_pizza = eval(input('Сколкьо стоит пицца в меню? '))
subtotal = number_pizzas * cost_pizza
tax_rate = 0.08
sale_tax = subtotal * tax_rate
total = subtotal + sale_tax
print('Полная стоимость заказа $',total)
print('в том числе налог$', sale_tax)
print('За пиццу отдельно $',subtotal)
