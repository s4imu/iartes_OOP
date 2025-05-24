from abc import ABC, abstractmethod


class Sensor(ABC):
    @property
    @abstractmethod
    def unidade(self):
        pass

    @unidade.setter
    @abstractmethod
    def unidade(self, unidade):
        pass

    @abstractmethod
    def ler_valor(self):
        pass


class SensorTemperatura(Sensor):
    def __init__(self, valor, unidade="libra"):
        self.__medida = valor
        self.__unidade = unidade

    def ler_valor(self):
        return self.__medida  # converte para PSI

    @property
    def unidade(self):
        return self.__unidade

    @unidade.setter
    def unidade(self, unidade):
        self.__unidade = unidade
