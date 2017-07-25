from idaapi import *
import os



def _make_func_name(_name, _addr):
    set_name(_addr, _name, SN_NOCHECK)


def _get_func_name(_addr, _path):
    f = open(_path)
 
    for line in f.readlines():
        if '0000000000%s ' % hex(_addr)[2:-1] in line:
            return _content_string   
        _content_string = line



def main():
    _start = cvar.inf.minEA
    _end = cvar.inf.maxEA
    _path_to_map = r'c:\Work\Temp\TEST\KssUiEngineGraphic.map'

    _func_addr = 0
    _index_func = 0
    while NextFunction(_func_addr) != '18446744073709551615':
        _func_addr = NextFunction(_func_addr)
        _func_name = _get_func_name(_func_addr, _path_to_map)
        if _func_name != None :
            _index_func += 1
            _make_func_name(_func_name[6:], _func_addr)
            print _index_func
    
main()
