from inspect import getmodule


def introspection_info(obj):
    return {'type': type(obj).__name__,
        'attributes': obj.__dict__,
        'methods': dir(obj),
        'module': getmodule(obj)}

class SomeСlass:
    def __init__(self):
        self.name = 'SomeClass'
        self.description = 4
        self.attributes = 30

obj = SomeСlass()


number_info = introspection_info(obj)
print(number_info)
