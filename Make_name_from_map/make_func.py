from idaapi import *
import os




def main():
    _start = cvar.inf.minEA
    _end = int (0x396DA8)

    for _addr in range(_start, _end -1):
    	_name = get_func_name(_addr)
    	if _name == None:
    		_add_next_func = NextFunction(_addr)
    		do_unknown_range(_addr, _add_next_func - _addr, DOUNK_EXPAND)
    		create_insn(_addr)
    		add_func(_addr, BADADDR)
    		print '%s %s' % (hex(_addr), hex(_end))



    
main()
