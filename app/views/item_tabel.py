from flet import *
from app.config.reference.ref import RefDataSiswa as RDS
from app.database.data_handler import data_handler
from app.views import sidebar
from app.views import data_siswa

class item_tabel(UserControl):
    def __init__(self,nisn,nama,jenis_kelamin,kelas,jurusan,page):
        super().__init__()
        self.nisn = nisn
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.kelas = kelas
        self.jurusan = jurusan
        self.page = page
     
    def build(self):
        return Row(spacing=0,
                                controls=[
                                    Container(border=border.only(bottom=border.BorderSide(1, "#022E57"),right=border.BorderSide(1, "#022E57"),left=border.BorderSide(1, "#DEECFF")),height=40,width=170,alignment=alignment.center,content=Text(color="#DEECFF",font_family="PoppinsMedium",size=13,value=self.nisn)),
                                    Container(border=border.only(bottom=border.BorderSide(1, "#022E57"),right=border.BorderSide(1, "#022E57")),height=40,width=200,padding=padding.symmetric(horizontal=10,vertical=10),content=Text(color="#DEECFF",font_family="PoppinsMedium",size=13,value=self.nama)),
                                    Container(border=border.only(bottom=border.BorderSide(1, "#022E57"),right=border.BorderSide(1, "#022E57")),height=40,width=170,alignment=alignment.center,content=Text(color="#DEECFF",font_family="PoppinsMedium",size=13,value=self.jenis_kelamin)),
                                    Container(border=border.only(bottom=border.BorderSide(1, "#022E57"),right=border.BorderSide(1, "#022E57")),height=40,width=130,alignment=alignment.center,content=Text(color="#DEECFF",font_family="PoppinsMedium",size=13,value=self.kelas)),
                                    Container(border=border.only(bottom=border.BorderSide(1, "#022E57"),right=border.BorderSide(1, "#022E57")),height=40,width=130,alignment=alignment.center,content=Text(color="#DEECFF",font_family="PoppinsMedium",size=13,value=self.jurusan)),
                                    Container(border=border.only(bottom=border.BorderSide(1, "#022E57"),right=border.BorderSide(1, "#022E57")),height=40,width=170,alignment=alignment.center,content=Row(alignment=MainAxisAlignment.CENTER,
                                            controls=[
                                                IconButton(
                                                    icon=icons.EDIT,
                                                    icon_color="#DEECFF",
                                                    icon_size=25,
                                                    tooltip="Edit",
                                                    on_click=lambda e:ubah_data(e,self.nisn,self.page)
                                                ),
                                                IconButton(
                                                icon=icons.DELETE_FOREVER_ROUNDED,
                                                icon_color=colors.RED_400,
                                                icon_size=28,
                                                tooltip="Delete",
                                                on_click =lambda e:open_modal(e,self.nisn,self.page)
                                                )
                                            ]
                                        )
                                    ),
                                ]
                            )

def open_modal(e,n,page):
    page.dialog = modal_delete(n,page)
    RDS.MODAL_DELETE.current.open = True
    RDS.MODAL_DELETE.current.data = n
    page.update()
    
def close_modal(x,page):
    RDS.MODAL_DELETE.current.open = False
    page.update()

def modal_delete(n,page):
    return AlertDialog(
                ref=RDS.MODAL_DELETE,
                modal=False,
                title=Text("Please confirm"),
                content=Text("Apakah Anda ingin menghapus data ini?"),
                actions = [
                    TextButton(text="Ya",on_click= lambda n:hapus_data(n,page)),
                    TextButton(text="Tidak",on_click= lambda n:close_modal(n,page))
                ],
                actions_alignment=MainAxisAlignment.END,
            )

def hapus_data(n,page:Page):
    data = RDS.MODAL_DELETE.current.data
    data_handler().hapus_data(data)
    close_modal(object(),page)
    data_siswa.data(page)
    page.views[0].controls = [Row(spacing=0,controls=[sidebar.view,Column(height=700,alignment=MainAxisAlignment.SPACE_BETWEEN,spacing=0,controls=[data_siswa.view_data,data_siswa.data_tabel])])]
    page.update()

def ubah_data(e,n,page):
    page.data = n
    page.go('/ubah-data')
    page.update()