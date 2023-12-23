def travel (bike=True,car=False):
  plan_travel=bike or car
  return bike, car,plan_travel
travel()
travel(False)
travel(_,True)
