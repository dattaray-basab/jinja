from soft_gen.source.code_gen.main import fn_getenv
from src.misc.persons import persons

env = fn_getenv()

file_path = 'content2.html'

tm = env.get_template(file_path)
msg = tm.render({'users': persons})

print(msg)
