from flet import *
from app.database.data_handler import data_handler
from app.config.reference.ref import RefTambahData as RTD

def view_tambah_data(page):
    width_box = page.window_width -250
    tb_nisn = TextField(autofocus=True,height=55,label="NISN",bgcolor="#DEECFF",border_color="#DEECFF",color="#E91E63",focused_border_color="#E91E63",label_style=TextStyle(color="#E91E63",font_family="PoppinsSemiBold"),text_style=TextStyle(font_family="PoppinsSemiBold"))
    tb_nama = TextField(height=55,label="Nama",bgcolor="#DEECFF",border_color="#DEECFF",color="#E91E63",focused_border_color="#E91E63",label_style=TextStyle(color="#E91E63",font_family="PoppinsSemiBold"),text_style=TextStyle(font_family="PoppinsSemiBold")) 
    tb_jenis_kelamin = RadioGroup(content=
                            Row(spacing=20,controls=[
                                Radio(value='Laki-Laki', label="Laki-Laki"),
                                Radio(value='Perempuan', label="Perempuan")
                                ]
                            )
                        )
    tb_kelas = Dropdown(label='Kelas',height=55,filled=True,bgcolor="#DEECFF",border_color="#DEECFF",color="#E91E63",focused_border_color="#E91E63",label_style=TextStyle(color="#E91E63",font_family="PoppinsSemiBold"),text_style=TextStyle(font_family="PoppinsSemiBold"),options=[dropdown.Option("10"),dropdown.Option("11"),dropdown.Option("12")])
    tb_jurusan = Dropdown(label='Jurusan',height=55,filled=True,bgcolor="#DEECFF",border_color="#DEECFF",color="#E91E63",focused_border_color="#E91E63",label_style=TextStyle(color="#E91E63",font_family="PoppinsSemiBold"),text_style=TextStyle(font_family="PoppinsSemiBold"),options=[dropdown.Option("TKJ"),dropdown.Option("TPM"),dropdown.Option("DPIB"),dropdown.Option("TKP"),dropdown.Option("TITL"),dropdown.Option("TKR"),dropdown.Option("KI")])
    
    return Container(width=width_box,height=700,padding=padding.only(right=400,left=20,top=20),bgcolor="#29ADB2",content=
        Container(content=Column(spacing=30,controls=[
        Row(spacing=0, controls=[
                    Container(margin=5, content= Icon(name="add",size=30,color="#E91E63")),
                    Container(content= Text(
                                "Tambah Data",
                                size=33,
                                color='#DEECFF',
                                font_family="PoppinsSemiBold"))    
                ]),
        tb_nisn,
        tb_nama,
        tb_jenis_kelamin,
        tb_kelas,
        tb_jurusan,
        Row(spacing=15,controls=[ElevatedButton(text="Kembali",on_click=lambda e:route_back(e,page)),ElevatedButton(bgcolor="#E91E63",text="Simpan",on_click=lambda e:simpan(e,tb_nisn,tb_nama,tb_jenis_kelamin,tb_kelas,tb_jurusan,page))]),

        ])))

def simpan(e,tb_nisn,tb_nama,tb_jenis_kelamin,tb_kelas,tb_jurusan,page:Page):
    nisn = str(tb_nisn.value)
    nama = str(tb_nama.value)
    jenis_kelamin = str(tb_jenis_kelamin.value)
    kelas = str(tb_kelas.value)
    jurusan = str(tb_jurusan.value)
 
    if nisn and nama and jenis_kelamin and kelas and jurusan == "" or len(nisn) != 10 or nisn.isalpha() or nama.isdigit():
        open_modal_error(page)
    else:
        data_handler().tambah_data(nisn,nama,jenis_kelamin,kelas,jurusan)
        open_modal_success(page)
        page.update()

def route_back(e,page:Page):
    page.go("/data-siswa")
    page.update()
    
def modal_error(page):
    return AlertDialog(
            ref=RTD.MODAL_ERROR,
            modal=False, 
            content=Text("Masukkan Data dengan Benar!!",size=20),
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

def open_modal_error(page):
    page.dialog = modal_error(page)
    RTD.MODAL_ERROR.current.open = True
    page.update()
    
def modal_success(page):
    return AlertDialog(
            ref=RTD.MODAL_SUCCESS,
            modal=False, 
            content=Text("Data Berhasil Ditambahkan",size=20),
            actions= [TextButton(text='Oke',on_click=lambda e:route_back(e,page))],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
    
def open_modal_success(page):
    page.dialog = modal_success(page)
    RTD.MODAL_SUCCESS.current.open = True
    page.update()