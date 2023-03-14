# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:16:38 2022

@author: ilara
"""

import sys
import numpy as np
import pickle

from syllabus import Syllabus
from squadron import Squadron
from simulation import Simulation

rng = np.random.default_rng()


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return


"""
F-35 Changes:
- Syllabus durations
- Turn pattern?
- Sq size
"""

f35_syllabi = {s.name: s for s in [Syllabus('MQT', 5, 'WG'),
               Syllabus('FLUG', 10, 'FL'),
               Syllabus('IPUG', 8, 'IP')]}

for syll in f35_syllabi.values():
    syll.capacity = 4

f35_sq = Squadron('f35_sq', syllabi=f35_syllabi)

api1_pilots = 24
api1_exp_pct = 0.4
api6_pilots = 8
api6_exp_pct = 1.0

initial_pilots = api1_pilots + api6_pilots
initial_sq_exp_pct = (api1_pilots*api1_exp_pct + api6_pilots*api6_exp_pct) / initial_pilots

f35_sq.populate_initial(initial_pilots, prop_EXP=initial_sq_exp_pct, prop_IP=0.25)
# f35_sq.print_()

"""
Simulation Setup
"""

sim = Simulation()
sim.setup(starting_sq=f35_sq)

# sim.sq.print_()

num_runs = 100
months_per_run = 60

"""
Scenario Inputs
"""


#NUM_YEARS = 5
# Start rig
ftu_arrivals = [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1] #*NUM_YEARS
nth_arrivals = [0, 2, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0] #*NUM_YEARS

# turn pattern
tails_go_1 = 8
tails_go_2 = 6
monthly_fly_days = 20

sortie_generation = [(tails_go_1 + tails_go_2)*monthly_fly_days]*12 #*NUM_YEARS

tos_threshold = 36

# # for ftu, nth, sorties in zip(ftu_arrivals, nth_arrivals, sortie_generation):
# #     sim.step_month(inflow_ftu=ftu, inflow_nth=nth, sorties_avail=sorties, tos_threshold=30)

# #sim.monthly_stats

# per_pilot = sim.per_pilot_stats
# monthly = sim.monthly_stats
# monthly.keys()

"""
Run the simulation many times
"""

many = sim.many_runs(ftu_arrival_calendar=ftu_arrivals,
                     nth_arrival_calendar=nth_arrivals,
                     sortie_generation_calendar=sortie_generation,
                     num_runs=num_runs,
                     months_per_run=months_per_run,
                     tos_threshold=tos_threshold)

with open('sim_data.pickle', 'wb') as datafile:
    pickle.dump(many, file=datafile)
