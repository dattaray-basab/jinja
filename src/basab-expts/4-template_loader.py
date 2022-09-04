from jinja2 import Environment, FileSystemLoader, FunctionLoader

# FileSystemLoader
persons = [
    {'name': 'Alex', 'age': 18, 'weight': 78.5},
    {'name': 'Niko', 'age': 20, 'weight': 92.1},
    {'name': 'Ivan', 'age': 39, 'weight': 83.9}
]
file_loader = FileSystemLoader('../templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons)
print(msg)


# FunctionLoader
def load_template(path):
    if path == 'index':
        return '''Имя {{ user.name }}, возраст {{ user.age }}.'''
    else:
        return '''Данные: {{ user }}'''


file_loader = FunctionLoader(load_template)
env = Environment(loader=file_loader)

tm = env.get_template('index')
msg = tm.render(user=persons[0])
print(msg)
