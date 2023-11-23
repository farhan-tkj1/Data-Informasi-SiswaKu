import json
# from app.database.data_handler import data
# from app.views.data_siswa import view


class manajemen_data():
    def __init__(self):
        self.data_original = {}
        self.baca_data()
        self.data_filtered = {}
        self.data_filtered = dict(self.data_original)
  

    def baca_data(self):
        try:
            with open("app/database/Data_Siswa.json", 'r') as file:
                self.data_original = json.load(file)
        except FileNotFoundError:
            pass
       
    # def reset_table(self):
    #     self.baca_data
    #     print(self.data_original)

    # def update_table(self):
    #     return self.filtered_students
       
    def search_data(self,query)->None:
        self.key = query
        self.data_filtered = {k:v for k,v in self.data_filtered.items() if self.key.lower() in v.get('Nama').lower()}
        # for item in self.tree.get_children():
            # self.tree.delete(item)
        # data = 0
        # for key, student in self.data_filtered.items():
        #     data +=1
        #     self.tree.insert("", "end", values=(data, key, student["Nama"], student["Jenis Kelamin"],
        #                                         student["Kelas"], student["Jurusan"]))
        
    def filter_byKelas(self, event):
        selected_filter = str(self.filter_kelas.get())
        selected_filter_jurusan = self.filter_jurusan.get()
        if selected_filter_jurusan == "All":
            if selected_filter == "All":
                self.filtered_students = self.students.copy()
            else:
                self.filtered_students = {key: value for key, value in self.students.items() if str(value['Kelas']) == selected_filter}
        else:
            if selected_filter == "All":
                self.filtered_students = {key: value for key, value in self.students.items() if value['Jurusan'] == selected_filter_jurusan}
            else:
                self.filtered_students = {key: value for key, value in self.students.items() if str(value['Kelas']) == selected_filter and value['Jurusan'] == selected_filter_jurusan}
        print(self.data_filtered)
        

    def filter_byJurusan(self,event):
        selected_filter = self.filter_jurusan.get()
        selected_filter_kelas = str(self.filter_kelas.get())
        if selected_filter_kelas == "All":
            if selected_filter == "All":
                self.filtered_students = self.students.copy()
            else:
                self.filtered_students = {key: value for key, value in self.students.items() if value['Jurusan'] == selected_filter}
        else:
            if selected_filter == "All":
                self.filtered_students = {key: value for key, value in self.students.items() if str(value['Kelas']) == selected_filter_kelas}
            else:
                self.filtered_students = {key: value for key, value in self.students.items() if value['Jurusan'] == selected_filter and str(value['Kelas']) == selected_filter_kelas}
        self.update_table()
            

    def sort_data(self):
        return {k: v for k, v in sorted(app.data_original.items(), key=lambda v: v[1].get('Nama'))}
        


app = manajemen_data()
original = app.data_original
filtered = app.data_filtered


