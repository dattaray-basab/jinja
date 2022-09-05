def token_mgr():
    def fn_get_tokens():
        tokens = {'users': [
            {'name': 'Alex', 'age': 18, 'weight': 78.5},
            {'name': 'Nikolas', 'age': 20, 'weight': 92.1},
            {'name': 'Ivan', 'age': 39, 'weight': 83.9}
        ]}
        return tokens

    return  fn_get_tokens