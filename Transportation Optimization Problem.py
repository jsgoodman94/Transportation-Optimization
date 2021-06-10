#!/usr/bin/env python
# coding: utf-8

# Transportation problem - using integer linear programming
# 
# Tropicsun is a distributor of citrus products, with three large groves scattered around central Floria in the cities of Mt.Dota, Eustis,and Clermont. Tropicsun currently has 275,000 bushles of citrus at the grove in Mt.Dora, 400,000 bushes at the grove in Eustis, and 300,000 at the grove in Clermont.
# 
# Tropicsun has processing plants in Ocala, Orlando and Lessburg with processing capacities to handle 200,000, 600,000, and 225,000 bushels. The local trucking company charges a flat per mile rate for each bushel (bushel-mile). The miles between the groves and processing planets are summarized below:
# 
# 
# Ocala
# 
# Mt.Dora - 21
# Eustis - 35
# Clermont - 55
# 
# Orlando
# 
# Mt.Dora - 50
# Eustis - 30
# Clermont - 20
# 
# Leesburg
# 
# Mt.Dora - 40
# Eustis - 22
# Clermont - 25
# 
# 
# Objective: determine how many bushels to ship from each grove to each planet to minimize the number of bushel miles.

# In[3]:


from pulp import *

GROVES = ['Mt.Dora','Eustis','Clermont']
PLANTS = ['Ocala','Orlando','Leesburg']

#dictionary of max amount of bushels that can be shipped to each plant
mship = {'Ocala':200000,
         'Orlando':600000,
         'Leesburg':225000}

#dictionary of what each grove will supply
supply = {'Mt.Dora':275000,
         'Eustis':400000,
         'Clermont':300000}

# dictionary of bushel miles
bush = {'Mt.Dora':{'Ocala':21,'Orlando':50,'Leesburg':40},
        'Eustis':{'Ocala':35,'Orlando':30,'Leesburg':22},
        'Clermont':{'Ocala':55,'Orlando':20,'Leesburg':25}}

# set problem variable
prob = LpProblem("Transportation",LpMinimize)

#create routes list from lists above - all combinations
routes = [(i,j) for i in GROVES for j in PLANTS]
#decision variable
amount_vars = LpVariable.dicts("ShipAmount",(GROVES,PLANTS),0)

#objective function
prob += lpSum(amount_vars[i][j]*bush[i][j] for (i,j) in routes)

#constraints
for j in PLANTS:
    prob += lpSum(amount_vars[i][j] for i in GROVES) <= mship[j]
   
for i in GROVES:
    prob += lpSum(amount_vars[i][j] for j in PLANTS) == supply[i]
   
#solve
prob.solve()

for v in prob.variables():
    if v.varValue > 0:
        print(v.name,"=",v.varValue)
print("Total bushel-miles=",value(prob.objective))

