# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 13:21:05 2025

@author: anees
"""

import numpy as np
from numba import njit
    
class SystemJit:
    def __init__(self, initialPosition, initialVelocity = 0, initialAcceleration = 0, 
                 springConstant = 100, dampingConstant = 3, thresholdVelocity = 1.0, 
                 simulationLength = 10, timeInterval = .0001, scale = True):
        #initial conditions
        self.initialPosition = initialPosition
        self.initialVelocity = initialVelocity
        self.initialAcceleration = initialAcceleration
        
        #system properties
        self.springConstant = springConstant
        self.dampingConstant = dampingConstant
        self.thresholdVelocity = thresholdVelocity 
        
        #simulation parameters
        self.simulationLength = simulationLength 
        self.timeInterval = timeInterval
        self.timeVector = np.arange(0, self.simulationLength, self.timeInterval)
        
        #perform simulation
        timeVector = np.arange(0, simulationLength, timeInterval)
        self.positionVector = SystemJit.simulate(timeVector, initialPosition, 
                                            initialVelocity, initialAcceleration, 
                                            thresholdVelocity, dampingConstant,
                                            springConstant, timeInterval)
        if scale:
            self.maxDisplacement = np.max(self.positionVector)
            self.positionVector = np.divide(self.positionVector, self.maxDisplacement) 
    
    @staticmethod
    @njit
    def simulate(timeVector, initialPosition, initialVelocity, initialAcceleration, 
                 thresholdVelocity, dampingConstant, springConstant, timeInterval):
        positionVector = np.zeros_like(timeVector)
        velocity = initialVelocity 
        acceleration = initialAcceleration
        position = initialPosition
        positionVector[0] = initialPosition
        
        for timeStep in range(len(timeVector)):
            if (timeStep == 0):
                continue
            
            #calculate friction
            if velocity > thresholdVelocity:
                friction = -dampingConstant * velocity
            else:
                friction =  -dampingConstant * thresholdVelocity * np.sign(velocity) 
            
            acceleration = friction - (springConstant * position)
            velocity = velocity + (acceleration * timeInterval)
            position = position + (velocity* timeInterval)
            positionVector[timeStep] = position
            
        return positionVector