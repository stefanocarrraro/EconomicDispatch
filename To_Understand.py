from pyomo.environ import *
from pyomo.opt import SolverStatus, TerminationCondition
import pandas, numpy
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import numpy as np

#This is a custom function that writes all the decision variables to an excel file.
#from Helper_Functions.exportDecisionVariables import exportDecisionVariables

filename = 'Assignment3_ValidationSystem.xlsx'

SystemDemand= pandas.read_excel(filename, sheet_name = 'SystemDemand', index_col= 0)

model.T = Set(ordered = True, initialize = SystemDemand.index) #Set for time steps 
print(model.T)	