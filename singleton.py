class Singleton(type):
    """
    This class is a prototype for creating singleton class.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instantiated_object = super(Singleton, cls).__call__(*args, **kwargs)

            cls._instances[cls] = instantiated_object
        return cls._instances[cls]
