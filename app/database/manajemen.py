import json
from app.database.data_handler import data_handler
# from app.views.data_siswa import view


class manajemen_data():
    def __init__(self):
        self.data_original = {}
        self.data_original = dict(data_handler().data_siswa)
       
    def search_data(self,query,source)->None:
        self.key = query
        if self.key.isdigit():
            return {k:v for k,v in source.items() if self.key.lower() in k.lower()}
        else:    
            return {k:v for k,v in source.items() if self.key.lower() in v.get('Nama').lower()}
        

            
    def filter(self,kelas,jurusan):
        if kelas == "All":
            if jurusan == "All":
                return self.data_original
            else:
                return {key: value for key, value in self.data_original.items() if value['Jurusan'] == jurusan}
        else:
            if jurusan == "All":
                return {key: value for key, value in self.data_original.items() if str(value['Kelas']) == kelas}
            else:
                return {key: value for key, value in self.data_original.items() if str(value['Kelas']) == kelas and value['Jurusan'] == jurusan}
        
    def sort_data(self,result):
        return {k: v for k, v in sorted(result.items(), key=lambda v: v[1].get('Nama'))}
        



