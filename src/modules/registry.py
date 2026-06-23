from typing import Dict, Type

from src.modules.base import HeadModule


class ModuleRegistry:
    _modules: Dict[str, Type[HeadModule]] = {}

    @classmethod
    def register(cls, name: str, module_class: Type[HeadModule]):
        cls._modules[name] = module_class

    @classmethod
    def get(cls, name: str) -> Type[HeadModule]:
        if name not in cls._modules:
            raise ValueError(f"Unknown head module: {name}")
        return cls._modules[name]

    @classmethod
    def list_modules(cls):
        return list(cls._modules.keys())
