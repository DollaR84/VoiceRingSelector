from dataclasses import dataclass, field


@dataclass(slots=True)
class Config:
    required_languages: list[str] = field(default_factory=list)
    required_voices: list[str] = field(default_factory=list)
