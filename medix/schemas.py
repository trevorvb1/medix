from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Entity(BaseModel):

    class MatchLevel(int, Enum):
        # TO DO
        Exact = 0
        Close = 1
        Partial = 2
        Broad_loose = 3

    class MatchType(int, Enum):
        """
        (0) Real: An index info from a linearization entity
        (1) UnderShoreLine: An index entity from an entity under the shoreline
        (2) UnderShoreLineLogicallyDefined: An index entity from an entity under the shoreline and has a logical definition
        (3) PostCoordinationCombination: Virtual index entity created by following post-coordination combinations
        """
        Real = 0
        UnderShoreLine = 1
        UnderShoreLineLogicallyDefined = 2
        PostCoordinationCombination = 3

    matching_text: Optional[str]
    code: Optional[str]
    foundation_uri: Optional[str]
    linearization_uri: Optional[str]
    match_level: MatchLevel
    match_score: float
    match_type: MatchType