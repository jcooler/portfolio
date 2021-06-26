weight = 41.5

flat_charge = 20.00

premium_cost = 125.00





#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + flat_charge
elif (weight > 2) and (weight <= 6):
  cost_ground = weight * 3.00 + flat_charge
elif (weight > 6) and (weight <= 10):
  cost_ground = weight * 4.00 + flat_charge
elif (weight > 10):
  cost_ground = weight * 4.75 + flat_charge
else:
  print("error")

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif (weight > 2) and (weight <= 6):
  cost_drone = weight * 9.00
elif (weight > 6) and (weight <= 10):
  cost_drone = weight * 12.00
elif (weight > 10):
  cost_drone = weight * 14.25
else:
  print("error")

print(cost_ground)