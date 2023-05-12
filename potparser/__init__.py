__all__ = ['parser']

for module in __all__:
    exec(f"from .{module} import *")