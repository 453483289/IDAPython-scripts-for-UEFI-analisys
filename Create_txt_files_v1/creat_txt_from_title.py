#-*- coding: cp866 -*-

from idaapi import * 



# ����뢠�� 䠩� � ���७��� '.i64', ��࠭�� ���� ������.
# ᮧ���� '.i64' �� '.bin'
def _close_programm():
    qexit(0)


      
# ��� ���� ����⮣� 䠩�� '.i64' ��� �室� (EntryPoint),
# �᫨ ��室�� (�� PE/TE) - ������� �� ��� �������਩, �᫨
# �� ��室�� (�� ROW) - ������� �������਩ ��⠭�������
# �� ᠬ� ����訩 ���� 䠩��. ��४������ �� cp866 � cp1251
# (cp866 �� ����⥭ ����樮���� ��⥬�)
def _find_comment():
    _comm = ''
    if get_entry_qty() == 1:
        _comm = GetFunctionCmt(get_entry_ordinal(0), 1)
    else:
        _str = ''
        for i in range(0,100):
            if get_extra_cmt(0, idaapi.E_PREV + i) != None:
                _str += get_extra_cmt(0, idaapi.E_PREV + i)
                if _str[-1:] != ' ':
                    _str += ' '
    return _str.decode('cp866').encode('cp1251')


        
#
#    �������� �������
#
#
# ����᪠���� ����� ����⮣� '.i64' 䠩��. ����砥� ��� 䠩��,
# ᮧ���� ⥪�⮢� ���㬥�� � ⠪�� �� ������. ��室�� � '.i64'
# �������਩ �� ����� �㭪樨 '_find_comment()', �����뢠��
# �������� �������਩ � ⥪�⮢� 䠩�. ����뢠�� '.i64'
def main():
    _file_name = get_root_filename()
    _file = open('%s.txt' % _file_name[:-4], 'w')
    _comment = _find_comment()
    _file.write('%s' % _comment)
    _close_programm()



# ��窠 ���� �ணࠬ��.    
main()
