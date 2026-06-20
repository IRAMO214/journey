weight = 41.5
#ground shipping
if weight <= 2:
  price = 1.5
elif weight > 2 and weight <= 6:
  price = 3.0
elif weight > 6 and weight <= 10:
  price = 4.0
else:
  price = 4.75
print("cost of ground shipping is: ", weight * price + 20)
#Ground shipping Premium
cost = 125.00
print("Cost of ground shippng premium shipping is: ", cost)

#Drone Shipping
if weight <= 2:
  price = 4.5
elif weight > 2 and weight <= 6:
  price = 9.0
elif weight > 6 and weight <= 10:
  price = 12.0
else:
  price = 14.25

print("Cost of drone shippng is: ", weight * price)
