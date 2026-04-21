from dataclasses import dataclass

@dataclass(frozen=True)
class MEQOption:
    label: str
    value: int

@dataclass(frozen=True)
class MEQQuestion:
    id: str
    number: int
    category: str
    prompt: str
    options: list[MEQOption] 

@dataclass(frozen=True)
class InterpretationBand:
    score_min: int
    score_max: int
    code: str
    label: str

@dataclass(frozen=True)
class MEQInstrument:
    id: str
    name: str
    version: str
    citation: str
    copyright: str
    score_min: int
    score_max: int
    scoring_method: str
    questions: list[MEQQuestion]
    bands: list[InterpretationBand]

