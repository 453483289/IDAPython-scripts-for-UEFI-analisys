# -*- coding: cp866 -*-

import os
import subprocess



# �ਭ����� �� �室 ��� � ���� � 䠩�� � ���७��� '.i64', ���뢠�� ��� �
# ����᪠�� �ᯮ����⥫�� �ਯ�, ����� ࠡ�⠥� ����� IdaPro.
def _start_i64(_name_i64, _path_to_i64, _path_to_py):
    subprocess.call("idaq64 -S\"%s\creat_txt_from_title.py\" \"%s\\%s\"" % (_path_to_py, _path_to_i64, _name_i64), shell=True)



#
#    �������� �������
#
# ��⠫������� �� 㪠������ ��४�ਨ '_dst_dir', �஡����� �� �ᥬ �������� ������
# �, �᫨ ��室�� 䠩� � ���७��� '.i64', ��।��� ��� 䠩��, ���� � ���� � ����
# � �ᯮ����⥫쭮�� 䠩�� '.py' � �㭪�� '_run_i64()'.
def main():
    _src_dir = os.getcwd()
    _dst_dir = r'c:\Users\Kyurchenko\Downloads\\' 
    for _path, _dirictories, _files in os.walk(_dst_dir):
        for _name in _files:
            if _name[-4:]=='.i64':
                _start_i64(_name, _path, _src_dir)



# ��窠 ���� �ணࠬ��.
main()
