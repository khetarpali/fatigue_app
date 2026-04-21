from dataclasses import dataclass

@dataclass(frozen=True)
class ChronotypeResult:
    score : int
    band_code : str
    band_label : str
