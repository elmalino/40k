from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Figurine:
    """Represent a single Age of Sigmar figurine."""
    name: str
    faction: str

# A non-exhaustive sample of Age of Sigmar figurines
FIGURINES: List[Figurine] = [
    Figurine(name="Liberators", faction="Stormcast Eternals"),
    Figurine(name="Judicators", faction="Stormcast Eternals"),
    Figurine(name="Retributors", faction="Stormcast Eternals"),
    Figurine(name="Ardboys", faction="Orruk Warclans"),
    Figurine(name="Brutes", faction="Orruk Warclans"),
    Figurine(name="Savage Orruks", faction="Orruk Warclans"),
    Figurine(name="Chainrasps", faction="Nighthaunt"),
    Figurine(name="Grimghast Reapers", faction="Nighthaunt"),
    Figurine(name="Hexwraiths", faction="Nighthaunt"),
    Figurine(name="Saurus Warriors", faction="Seraphon"),
    Figurine(name="Skinks", faction="Seraphon"),
    Figurine(name="Bastiladon", faction="Seraphon"),
]
