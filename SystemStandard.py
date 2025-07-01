# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 13:19:00 2025

@author: anees
"""

import numpy as np

class SystemStandard:
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
        self.positionVector = self.simulate(initialPosition, initialVelocity, initialVelocity)
        if scale:
            self.maxDisplacement = np.max(self.positionVector)
            self.positionVector = np.divide(self.positionVector, self.maxDisplacement) 
        
    def friction(self, velocity):
        if velocity > self.thresholdVelocity:
            return -self.dampingConstant * velocity
        else:
            return -self.dampingConstant * self.thresholdVelocity * np.sign(velocity) 
        
    def simulate(self, initialPosition, initialVelocity, initialAcceleration):
        positionVector = np.zeros_like(self.timeVector)
        velocity = initialVelocity 
        acceleration = initialAcceleration
        position = initialPosition
        positionVector[0] = initialPosition
        
        for timeStep in range(len(self.timeVector)):
            if timeStep == 0:
                continue
            acceleration = self.friction(velocity) - (self.springConstant * position)
            velocity = velocity + (acceleration * self.timeInterval)
            position = position + (velocity* self.timeInterval)
            positionVector[timeStep] = position
            
        return positionVector