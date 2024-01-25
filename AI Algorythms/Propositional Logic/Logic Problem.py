from Copied.Logic import *

# Weather
rain = Symbol("raining")
snow = Symbol("snowing")
hot = Symbol("hot")
cold = Symbol("cold")

# Seasons
spring = Symbol("spring")
summer = Symbol("summer")
fall = Symbol("fall")
winter = Symbol("winter")

# if its hot then it's not cold
# if its raining then it's not snowing

# if (And(And(And(hot and not(cold)) and not(raining)) and not(snowing)) then its summer)
# it is summer

knowledge = And(Implication(And(And(And(hot, Not(cold)), And(Not(rain)), Not(snow))), summer))

print(knowledge.formula())
model_check(knowledge, summer)
