import sys
import pyswmm

try:
    pyswmm.Simulation('')
except pyswmm.swmm5.SWMMException:
    pass
