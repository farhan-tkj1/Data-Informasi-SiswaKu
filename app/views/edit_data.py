from flet import *
from app.database.data_handler import data_handler

def view_edit_data(page:Page):
    global result
    result = data_handler().seacrh_data(page.data)
    
    width_box = page.window_width -250
    tb_nisn = TextField(disabled=True,value=page.data,height=55,label="NISN",bgcolor="#DEECFF",border_color="#DEECFF",color="#E91E63",label_style=TextStyle(color="#E91E63",font_family="PoppinsSemiBold"),text_style=TextStyle(font_family="PoppinsSemiBold"))
    tb_nama = TextField(value=result['Nama'],height=55,label="Nama",bgcolor="#DEECFF",border_color="#DEECFF",color="#E91E63",label_style=TextStyle(color="#E91E63",font_family="PoppinsSemiBold"),text_style=TextStyle(font_family="PoppinsSemiBold")) 
    tb_jenis_kelamin = RadioGroup(value=result['Jenis Kelamin'],content=
                            Row(spacing=20,controls=[
                                Radio(value='Laki-Laki', label="Laki-Laki"),
                                Radio(value='Perempuan', label="Perempuan")
                                ]
                            )
                        )
    tb_kelas = Dropdown(filled=True,value=result['Kelas'],label='Kelas',height=55,bgcolor="#DEECFF",border_color="#DEECFF",color="#E91E63",label_style=TextStyle(color="#E91E63",font_family="PoppinsSemiBold"),text_style=TextStyle(font_family="PoppinsSemiBold"),options=[dropdown.Option("10"),dropdown.Option("11"),dropdown.Option("12")])
    tb_jurusan = Dropdown(filled=True,value=result['Jurusan'],label='Jurusan',height=55,bgcolor="#DEECFF",border_color="#DEECFF",color="#E91E63",label_style=TextStyle(color="#E91E63",font_family="PoppinsSemiBold"),text_style=TextStyle(font_family="PoppinsSemiBold"),options=[dropdown.Option("TKJ"),dropdown.Option("TPM"),dropdown.Option("DPIB"),dropdown.Option("TKP"),dropdown.Option("TITL"),dropdown.Option("TKR"),dropdown.Option("KI")])

    return Container(width=width_box,height=700,padding=padding.only(right=400,left=20,top=20),bgcolor="#29ADB2",content=
        Container(content=Column(spacing=30,controls=[
        Row(spacing=0, controls=[
                    Container(margin=5, content= Icon(name="add",size=30,color="#E91E63")),
                    Container(content= Text(
                                "Edit Data",
                                size=33,
                                color='#DEECFF',
                                font_family="PoppinsSemiBold"))    
                ]),
        tb_nisn,
        tb_nama,
        tb_jenis_kelamin,
        tb_kelas,
        tb_jurusan,
        Row(spacing=15,controls=[ElevatedButton(text="Kembali",on_click=lambda e:route_back(e,page)),ElevatedButton(bgcolor="#E91E63",text="Simpan",on_click=lambda e:update(e,page.data,str(tb_nama.value),str(tb_jenis_kelamin.value),str(tb_kelas.value),str(tb_jurusan.value),page))]),
        ])))
    
def update(e,nisn,nama,jenis_kelamin,kelas,jurusan,page:Page):
    data_handler().ubah_data(nisn,nama,jenis_kelamin,kelas,jurusan)
    page.go('/data-siswa')
    page.update()
   
def route_back(e,page:Page):
    page.go("/data-siswa")
    page.update()