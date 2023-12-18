import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
speed = ctrl.Consequent(np.arange(0, 101, 1), 'speed')
fan_power = ctrl.Consequent(np.arange(0, 101, 1), 'fan_power')

# Define fuzzy sets for temperature
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['medium'] = fuzz.trimf(temperature.universe, [0, 50, 100])
temperature['high'] = fuzz.trimf(temperature.universe, [50, 100, 100])

# Define fuzzy sets for speed
speed['low'] = fuzz.trimf(speed.universe, [0, 0, 50])
speed['medium'] = fuzz.trimf(speed.universe, [0, 50, 100])
speed['high'] = fuzz.trimf(speed.universe, [50, 100, 100])

# Define fuzzy sets for fan power
fan_power['low'] = fuzz.trimf(fan_power.universe, [0, 0, 50])
fan_power['medium'] = fuzz.trimf(fan_power.universe, [0, 50, 100])
fan_power['high'] = fuzz.trimf(fan_power.universe, [50, 100, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(temperature['low'] | temperature['medium'], speed['low'])
rule2 = ctrl.Rule(temperature['high'], speed['high'])

rule3 = ctrl.Rule(speed['low'], fan_power['low'])
rule4 = ctrl.Rule(speed['medium'], fan_power['medium'])
rule5 = ctrl.Rule(speed['high'], fan_power['high'])

# Create fuzzy system
fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2])
fan_power_ctrl = ctrl.ControlSystem([rule3, rule4, rule5])

# Create simulations
fan_speed_simulation = ctrl.ControlSystemSimulation(fan_speed_ctrl)
fan_power_simulation = ctrl.ControlSystemSimulation(fan_power_ctrl)

# Example usage
fan_speed_simulation.input['temperature'] = 75
fan_speed_simulation.compute()
print("Fan Speed:", fan_speed_simulation.output['speed'])

fan_power_simulation.input['speed'] = fan_speed_simulation.output['speed']
fan_power_simulation.compute()
print("Fan Power:", fan_power_simulation.output['fan_power'])
