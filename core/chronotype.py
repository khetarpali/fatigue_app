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