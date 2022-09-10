# This class allows dictionaries to be treated as object so that the dot
# notation can be used to access attributes

class DotDict(dict):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value
