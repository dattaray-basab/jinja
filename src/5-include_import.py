from jinja2 import Environment, FileSystemLoader

persons = [
    {'name': 'Alex', 'age': 18, 'weight': 78.5},
    {'name': 'Niko', 'age': 20, 'weight': 92.1},
    {'name': 'Ivan', 'age': 39, 'weight': 83.9}
]
domain = 'https://www.google.com'
dialog = {'title': 'Внимание!', 'msg': 'Это тестовый диалог'}

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(users=persons, domain=domain, title='Test page', dialog=dialog)
print(msg)
