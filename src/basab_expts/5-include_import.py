# import pathlib

from jinja2 import Environment, FileSystemLoader

# from src.basab_expts.Filters.str_ops import lower2
# from src.basab_expts.Filters.str_ops import filter_x1
from src.basab_expts.Filters.str_ops import filter_x1
from src.misc.persons import persons

dialog = {'title': 'basab title'}
# dialog = {'title': 'Внимание!', 'msg': 'Это тестовый диалог'}

file_loader = FileSystemLoader( 'Templates' )
env = Environment(loader=file_loader)
env.filters["filter_x1"] = filter_x1

tm = env.get_template('content2.html')
msg = tm.render(users=persons)
print(msg)
