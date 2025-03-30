# Bu modül FastAPI router'ını dışa aktarır
# routing.py'den router'ı import eder ve __all__ listesi ile
# bu modülden hangi nesnelerin dışa aktarılacağını belirtir
from .routing import router

__all__ = ["router"]
