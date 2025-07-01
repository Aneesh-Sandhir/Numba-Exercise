# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:38:26 2025

@author: anees
"""
from SystemStandard import SystemStandard
from SystemJit import SystemJit
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    simulation0, simulation1, simulation2 = SystemStandard(0.1), SystemStandard(1), SystemStandard(10)
    plt.plot(simulation0.timeVector, simulation0.positionVector)
    plt.plot(simulation1.timeVector, simulation1.positionVector)
    plt.plot(simulation2.timeVector, simulation2.positionVector)
    plt.title('Standard Output')
    plt.legend(['0.1', '1', '10'])
    plt.show()
    
    print('Processing time is roughly equal when the jitted class is called for the first time')
    
    %time _  = SystemStandard(0.1)
    %time _  = SystemJit(0.1)
    
    simulation0, simulation1, simulation2 = SystemJit(0.1), SystemJit(1), SystemJit(10)
    plt.plot(simulation0.timeVector, simulation0.positionVector)
    plt.plot(simulation1.timeVector, simulation1.positionVector)
    plt.plot(simulation2.timeVector, simulation2.positionVector)
    plt.title('Jit Output')
    plt.legend(['0.1', '1', '10'])
    plt.show()
    print('Outputs are Equal\n')
    
    print('Processing time is sigificantly reduced after the jitted class has been called for the first time')
    %time _  = SystemStandard(0.75)
    %time _  = SystemJit(0.75)
    
    