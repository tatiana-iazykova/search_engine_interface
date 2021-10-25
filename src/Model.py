from abc import ABC
from typing import List

class Model(ABC):

    def __init__(self):
        pass

    def fit(self, X: List[str]):
        pass

    def get_top_k(self, query:str, k:int = None) -> List[str]:
        """
        Function that returns ranked prediction given the request
        Optional parameter k to specify the length of the input
        
        Example:
        query = "kettle"
        k = 3

        ->

        ["pot", "kitchen utensils", "teapot"]
        """
        return []

