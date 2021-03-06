#!/usr/bin/python3

import sys, math
import matplotlib.pyplot as plt

sys.path.append("../")
from simulator import *


if __name__ == "__main__":

  # Alkaline battery
  # 10 Ohm continuous resistor load

  t, E_Batt, U_Batt, I_Batt = \
    Simulator(Alkaline(), ResistorLoad(10.0)).run()
  
  plt.xlabel('t [h]')
  plt.ylabel('$U_{Batt}$ [V]')
  plt.plot([x / 3600.0 for x in t], U_Batt)
  plt.show()
  
  plt.xlabel('$E_{Batt}$ [Wh]')
  plt.ylabel('$U_{Batt}$ [V]')
  plt.plot([x / 3600.0 for x in E_Batt], U_Batt)
  plt.show()
  
  plt.xlabel('t [h]')
  plt.ylabel('$I_{Batt}$ [mA]')
  plt.plot([x / 3600.0 for x in t], [x * 1000.0 for x in I_Batt])
  plt.show()
