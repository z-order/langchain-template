"""
Abstract class for the Maistro chatbot
"""

from abc import ABC, abstractmethod


class AbstractMaistro(ABC):
    @property
    @abstractmethod
    def graph(self):
        pass

    @property
    @abstractmethod
    def model(self):
        pass

    @property
    @abstractmethod
    def profile_extractor(self):
        pass
