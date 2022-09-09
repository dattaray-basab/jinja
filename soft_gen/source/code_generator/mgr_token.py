import json
import os

from soft_gen.source.common.dot_dict import DotDict


def token_mgr():
    def fn_get_tokens(token_dirpath):
        try:
            file_paths = []
            tokens = DotDict( {} )
            for root, directories, file in os.walk( token_dirpath ):
                for file in file:
                    if (file.endswith( ".json" )):
                        file_paths.append( os.path.join(root, file) )
            tokens = DotDict({})
            for filepath in file_paths:
                f = open( filepath)
                data = json.load( f )
                file_name, file_ext = os.path.basename(filepath).rsplit('.')
                tokens[file_name] = data

            return tokens

        except Exception as x:
            print(x)
            return None

    return  fn_get_tokens