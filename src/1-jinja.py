from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Alice', 33)

tm = Template('Hello! My name is {{ p.name.upper() }} and I am {{ p.age*2 }} years old')
msg = tm.render(p=p)

print(msg)
