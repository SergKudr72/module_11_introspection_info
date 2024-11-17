def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    attrs = [attr for attr in attributes if not callable(getattr(obj, attr))]
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__

    introsp_info = {'type': obj_type, 'attributes': attrs,
                    'methods': methods, 'module': module}

    return introsp_info


class Myclass:
    def __init__(self):
        self.name = 'Myclass'
        self.description = 100
        self.attributes = 1000

    def my_method(self):
        pass

obj = Myclass()

class_info = introspection_info(obj) # класс
print(class_info)

number_info = introspection_info(58) # число
print(number_info)

string_info = introspection_info('Urban') # строка
print(string_info)

list_info = introspection_info([1, 20, 4.0, 'word']) # список
print(list_info)

tuple_info = introspection_info((1, 5, 23, 'doc')) # кортеж
print(tuple_info)

