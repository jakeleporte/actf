# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:16:27 2022

@author: ilara
"""

class Syllabus:
    exp_sortie_rqmt = 250
    exp_qual_rqmt = 'FL'
    def __init__(self, name, duration, award):
        self.name = name
        self.duration = duration
        self.award = award
    @staticmethod
    def meets_EXP_criteria(pilot_sorties, pilot_qualifications):
        return (pilot_sorties >= Syllabus.exp_sortie_rqmt and
               Syllabus.exp_qual_rqmt in pilot_qualifications)
