from soft_gen.source.code_generator.mgr_codegen import codegen_mgr


fn_generate_code = codegen_mgr(__file__)

msg = fn_generate_code()

print(msg)
