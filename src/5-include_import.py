from jinja2 import Environment, FileSystemLoader

from src.misc.persons import persons

domain = 'https://www.google.com'
dialog = {'title': 'Внимание!', 'msg': 'Это тестовый диалог'}

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(users=persons, domain=domain, title='Test page', dialog=dialog)
print(msg)
