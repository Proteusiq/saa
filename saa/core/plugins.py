import importlib
import pkgutil
from saa import luga


def iter_luga_namespace(luga_package):
    return pkgutil.iter_modules(luga_package.__path__, luga_package.__name__ + ".")


supported_languages = {
    name[-2:]: importlib.import_module(name).Language
    for _, name, _ in iter_luga_namespace(luga)
}
