from pyswmm import Simulation
from pyswmm.tests.data import MODEL_WEIR_SETTING_PATH

sim = Simulation(MODEL_WEIR_SETTING_PATH)
sim.execute()
