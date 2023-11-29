from flet import *

class RefDataSiswa:
    MODAL_DELETE = Ref[AlertDialog]()
    
class RefTambahData:
    MODAL_ERROR = Ref[AlertDialog]()
    MODAL_SUCCESS = Ref[AlertDialog]()