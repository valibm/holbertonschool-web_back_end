#!/usr/bin/env python3
""" Somthing somthingson """
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ type-annotated function element_length """
    return [(i, len(i)) for i in lst]
