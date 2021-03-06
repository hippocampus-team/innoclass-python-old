import cffi
ffibuilder = cffi.FFI()


ffibuilder.embedding_api("""
    int do_stuff(int, int);
""")

ffibuilder.set_source("my_plugin", "")

ffibuilder.embedding_init_code("""
    from my_plugin import ffi

    @ffi.def_extern()
    def do_stuff(x, y):
        print("adding %d and %d" % (x, y))
        return x + y
""")

ffibuilder.compile(target="plugin-1.5.*", verbose=True)