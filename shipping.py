premium=125
def ground_shipping(weight):
  if weight<=2:
    cost=weight*1.5+20
  elif  weight>2 and weight<=6:
    cost=weight*3+20
  elif weight>6 and weight<=10:
    cost=weight*4+20
  else:
    cost=weight*4.75+20
  print(cost)
  return cost
ground=ground_shipping(4.8)

def drone_shipping(weight):
  if weight<=2:
    cost=weight*4.5
  elif  weight>2 and weight<=6:
    cost=weight*9
  elif weight>6 and weight<=10:
    cost=weight*12
  else:
    cost=weight*14.25
  print(cost)
  return cost
drone=drone_shipping(4.8)

def cheapest():
  if ground<drone and ground<premium:
    print("Ground is cheapest at a cost of"+str(ground))
  elif drone<ground and drone<premium:
    print("Drone is cheapest at a cost of"+str(drone))
  else:
    print("premium is cheapest at a cost of"+str(premium))
    
cheapest()
