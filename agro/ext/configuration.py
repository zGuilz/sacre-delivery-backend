from importlib import import_module

from dynaconf import FlaskDynaconf

def load_extensions(app):
    for extension in app.config.EXTENSIONS:
        # Splita a data que vem `ex.path:fact_func`
        module_name, factory = extension.split(":")
        # Importa dinamicamente o modulo
        ext = import_module(module_name)
        # Chama a função factory
        getattr(ext, factory)(app)

def init_app(app, **config):
    FlaskDynaconf(app, **config)
