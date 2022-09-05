# from soft_gen.source.code_gen.main import fn_getenv
from soft_gen.source.env_mgt.mgr_env import env_mgr
from src.basab_expts.Tokens.mgr_token import token_mgr

from src.misc.persons import persons

fn_getenv = env_mgr()
fn_get_tokens = token_mgr()

tokens = fn_get_tokens()

env = fn_getenv()

tm = env.get_template('content2.html')
msg = tm.render(tokens)

print(msg)
