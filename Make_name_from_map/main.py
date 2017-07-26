from idaapi import *
import os



_g_list = []



def _make_func_name(_name, _addr):
    if _name[-1:] == '\n':
        _name = _name[:-1]

    global _g_list

    if _name not in _g_list:
        _g_list.append(_name)
        set_name(_addr, _name, SN_NOCHECK)
    else:
        _name = _name + '_'
        _make_func_name(_name, _addr)

    



def _get_func_name(_addr, _path):
    f = open(_path)
 
    for line in f.readlines():
        if '0000000000%s ' % hex(_addr)[2:-1] in line:
            if line[:2] == ' .':
                return line[7:16]
            return _content_string[7:]   
        _content_string = line



def main():
    _start = cvar.inf.minEA
    _end = cvar.inf.maxEA
    _path_to_map = r'c:\Work\Temp\TEST\KssUiEngineGraphic.map'

    _func_addr = 0
    _index_func = 0
    while NextFunction(_func_addr) != BADADDR :
        _func_addr = NextFunction(_func_addr)
        _func_name = _get_func_name(_func_addr, _path_to_map)
        if _func_name != None :
            _index_func += 1
            _make_func_name(_func_name, _func_addr)
            print _index_func
    
main()
