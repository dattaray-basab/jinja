
from soft_gen.source.env_mgt.mgr_env import env_mgr
from src.basab_expts.Tokens.mgr_token import token_mgr


fn_getenv = env_mgr()
fn_get_tokens = token_mgr()

env = fn_getenv()

tm = env.get_template('content2.html')
tokens = fn_get_tokens()
msg = tm.render(tokens)

print(msg)