# coding: utf8

import os



def _find_dst_bin(_name_dir, _path):
	for _path_to_file, _dirictories, _files in os.walk(_path):
		if _name_dir[2:] in _path_to_file:
			print _path_to_file



def _take_dir_name(_path, _index):
	_lenth = len(_path)
	_end_index = _lenth
	_dir_name_list = []

	for _start_index in range(_lenth-1, 0, -1):
		if _path[_start_index] == '\\':
			_dir_name_list.append(_path[_start_index + 1 : _end_index])
			_end_index = _start_index

	return _dir_name_list[_index]



def _find_src_bin(_src, _dst):
	for _path_to_file, _dirictories, _files in os.walk(_src):
		for _file in _files:
			if _file[-4:] == '.bin':
				_dir_name = _take_dir_name(_path_to_file, 0)
				print _path_to_file
				_find_dst_bin(_dir_name, _dst)



def main():
	_src_path = r'c:\Work\Temp\TEST\KWQ170\3 BIOS region\4 FV 3\\'
	_dst_path = r'c:\Work\Temp\TEST\bios\3 BIOS\Fv3\\'
	_find_src_bin(_src_path, _dst_path)


	os.system('pause')



main()