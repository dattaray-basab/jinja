# import pathlib

from jinja2 import Environment, FileSystemLoader

from src.misc.persons import persons

dialog = {'title': 'basab title'}
# dialog = {'title': 'Внимание!', 'msg': 'Это тестовый диалог'}

file_loader = FileSystemLoader('./templates1')
env = Environment(loader=file_loader)

tm = env.get_template('content2.html')
msg = tm.render(users=persons)
print(msg)
