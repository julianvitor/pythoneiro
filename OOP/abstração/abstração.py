# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self._lado = lado
    
    def area(self):
        return self._lado * self._lado
    
    def perimetro(self):
        return self._lado * 4