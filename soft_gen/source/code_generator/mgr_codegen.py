from soft_gen.source.env_mgt.mgr_env import env_mgr
from src.basab_expts.Tokens.mgr_token import token_mgr


def codegen_mgr(caller_filepath):
    def fn_generate_code():
        fn_get_tokens = token_mgr()
        tokens = fn_get_tokens()
        fn_getenv = env_mgr()
        env = fn_getenv()
        tm = env.get_template( 'content2.x' )
        msg = tm.render( tokens )
        return msg
    return fn_generate_code