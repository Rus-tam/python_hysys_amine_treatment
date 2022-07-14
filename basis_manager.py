# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 19:32:07 2022

@author: Rustam
"""

from connector import Connector

class BasisManager:
    def __init__(self, case):
        self.case = case
    
    def setFldPackage(self):
        components = ['Methane', 'Ethane', 'Propane', 'i-Butane', 'n-Butane', 'H2O', 'MEAmine', 'CO2', 'H2S']
        root = self.case.BasisManager.FluidPackages
        
        print('--- Создаю Базис ----')
        print(' ')
        root.Add('Basis - 1')
        
        print('--- Задаю пакет свойств ----')
        print(' ')
        root.Item('Basis - 1').PropertyPackageName = 'acidgaspkg'
        
        print('--- Добавляю компоненты в список компонентов ---')
        print(' ')
        for component in components:
            root.Item('Basis - 1').ComponentList.Components.Add(component)
    

file_path = r'C:\Users\Rustam\Documents\second\1-1.hsc'
case = Connector.case(file_path)

basisManager = BasisManager(case)

basisManager.setFldPackage()

