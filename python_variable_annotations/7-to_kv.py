#!/usr/bin/env python3


"""
Docstring for python_variable_annotations.7-to_kv
"""


from typing import Union, Tuple



def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of the key and value
    """
    return (k, float(v * v))
