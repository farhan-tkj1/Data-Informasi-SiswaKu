import flet as ft
import json
from app.views.dashboard import view as dashboard
# from app.views.data_siswa.view import my_data
# from app.views.data_siswa.tambah import view
# from app.kelola.manajemen import original
from app.kelola.manajemen import filtered
from app.kelola import manajemen
from app.database.data_handler import data_handler

# my_data.__init__()

def main(page: ft.Page):
    page.title = "Data Informasi SiswaKu"
    page.padding = 0
    page.window_height = 740
    page.window_center()
    page.window_resizable = False
    page.window_maximizable  =False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {
        "FasterOne" : "config/fonts/FasterOne-Regular.ttf",
        "PoppinsSemiBold" : "config/fonts/Poppins-SemiBold.ttf",
        "PoppinsSemiBoldItalic" : "config/fonts/Poppins-SemiBoldItalic.ttf",
        "PoppinsMedium" : "config/fonts/Poppins-Medium.ttf"
    }
    global tabel_data,loop,original,baca
    
    def baca():
        global original
        try:
            with open("app/database/Data_Siswa.json", 'r') as file:
                original = json.load(file)
        except FileNotFoundError:
            pass
    baca()
    
    # Attribute
    labelMode = ft.Text(
                value="Mode",
                size=17,
                font_family="PoppinsSemiBold",
                color="#ffffff")  
    width_content = page.window_width-250
      
    # Fungsi Tambahan  
    def on_hover(e):
            e.control.bgcolor = ft.colors.RED_200 if e.data == "true" else ft.colors.TRANSPARENT
            # e.control.update()
    
    def change_mode(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()       

    # Delete Data
    def delete(no_induk):
        global tabel_data
        open_modal_del(no_induk)
        page.update()
    
    def delete_2(k):
        global tabel_data
        data_handler().hapus_data(k)
        tabel_data.clear()
        page.update()
        baca()
        tabel_data = loop(original)
        page.route = "/"
        page.update()
        
    
    def open_modal_del(k):
        global tabel_data
        page.dialog = ft.AlertDialog(
                            modal=False,
                            title=ft.Text("Please confirm"),
                            content=ft.Text("Apakah Anda ingin menghapus data ini?"),
                            actions = [
                                ft.TextButton(text="Ya",on_click= lambda e:delete_2(k)),
                                ft.TextButton(text="Tidak",)
                                ],
                            actions_alignment=ft.MainAxisAlignment.END,
                            on_dismiss=lambda e: print("Modal dialog dismissed!"),
                            open=True
                        )
            
        page.update()
    
    # Ubah Data
    def ubah_data(no):
        print('ubah',no)
        page.route = "/ubah-data"
        page.update()
    
    # Load Data
    def loop(data):
        print('memulai looping')
        tabel = [ft.Row(spacing=0,alignment=ft.MainAxisAlignment.CENTER,controls=[
                        ft.Container(border=ft.border.only(top=ft.border.BorderSide(1.3, "#74747B"),right=ft.border.BorderSide(1.3, "#74747B"),bottom=ft.border.BorderSide(1.3, "#74747B"),left=ft.border.BorderSide(1.3, "#74747B")),height=30,width=150,alignment=ft.alignment.center,content=ft.Text(size=15,font_family="PoppinsSemiBold",value='NISN')),
                        ft.Container(border=ft.border.only(top=ft.border.BorderSide(1.3, "#74747B"),right=ft.border.BorderSide(1.3, "#74747B"),bottom=ft.border.BorderSide(1.3, "#74747B")),height=30,width=250,alignment=ft.alignment.center,content=ft.Text(size=15,font_family="PoppinsSemiBold",value='Nama')),
                        ft.Container(border=ft.border.only(top=ft.border.BorderSide(1.3, "#74747B"),right=ft.border.BorderSide(1.3, "#74747B"),bottom=ft.border.BorderSide(1.3, "#74747B")),height=30,width=170,alignment=ft.alignment.center,content=ft.Text(size=15,font_family="PoppinsSemiBold",value='Jenis Kelamin')),
                        ft.Container(border=ft.border.only(top=ft.border.BorderSide(1.3, "#74747B"),right=ft.border.BorderSide(1.3, "#74747B"),bottom=ft.border.BorderSide(1.3, "#74747B")),height=30,width=130,alignment=ft.alignment.center,content=ft.Text(size=15,font_family="PoppinsSemiBold",value='Kelas')),
                        ft.Container(border=ft.border.only(top=ft.border.BorderSide(1.3, "#74747B"),right=ft.border.BorderSide(1.3, "#74747B"),bottom=ft.border.BorderSide(1.3, "#74747B")),height=30,width=130,alignment=ft.alignment.center,content=ft.Text(size=15,font_family="PoppinsSemiBold",value='Jurusan')),
                        ft.Container(border=ft.border.only(top=ft.border.BorderSide(1.3, "#74747B"),right=ft.border.BorderSide(1.3, "#74747B"),bottom=ft.border.BorderSide(1.3, "#74747B")),height=30,width=150,alignment=ft.alignment.center,content=ft.Text(size=15,font_family="PoppinsSemiBold",value='Action'))]),]
        for k,i in data.items() :
            tabel.append(ft.Row(spacing=0,alignment=ft.MainAxisAlignment.CENTER,controls=[
                            ft.Container(border=ft.border.only(bottom=ft.border.BorderSide(1, "#74747B"),right=ft.border.BorderSide(1, "#74747B"),left=ft.border.BorderSide(1, "#74747B")),height=40,width=150,alignment=ft.alignment.center,content=ft.Text(size=13,value=k)),
                            ft.Container(border=ft.border.only(bottom=ft.border.BorderSide(1, "#74747B"),right=ft.border.BorderSide(1, "#74747B")),height=40,width=250,padding=ft.padding.symmetric(horizontal=10,vertical=10),content=ft.Text(size=13,value=i['Nama'])),
                            ft.Container(border=ft.border.only(bottom=ft.border.BorderSide(1, "#74747B"),right=ft.border.BorderSide(1, "#74747B")),height=40,width=170,alignment=ft.alignment.center,content=ft.Text(size=13,value=i['Jenis Kelamin'])),
                            ft.Container(border=ft.border.only(bottom=ft.border.BorderSide(1, "#74747B"),right=ft.border.BorderSide(1, "#74747B")),height=40,width=130,alignment=ft.alignment.center,content=ft.Text(size=13,value=i['Kelas'])),
                            ft.Container(border=ft.border.only(bottom=ft.border.BorderSide(1, "#74747B"),right=ft.border.BorderSide(1, "#74747B")),height=40,width=130,alignment=ft.alignment.center,content=ft.Text(size=13,value=i['Jurusan'])),
                            ft.Container(border=ft.border.only(bottom=ft.border.BorderSide(1, "#74747B"),right=ft.border.BorderSide(1, "#74747B")),height=40,width=150,alignment=ft.alignment.center,content=ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_color="383838",
                                    icon_size=25,
                                    tooltip="Edit",
                                    on_click=lambda e:ubah_data(i['Nama'])
                                ),
                                ft.IconButton(
                                icon=ft.icons.DELETE_FOREVER_ROUNDED,
                                icon_color=ft.colors.RED_400,
                                icon_size=28,
                                tooltip="Delete",
                                on_click =lambda e:delete(k)
                                )]
                                )),
                            ]
                        )
                    )
        print('looping berhasil')
        return tabel
    tabel_data = loop(original)
    
    # Route 
    def go_dashboard(rute):
        page.route = "/"
        page.update()
    def go_data(rute):
        page.route = "/data-siswa"
        page.update()
    def go_tentang(rute):
        page.route = "/tentang"
        page.update()
    def go_tambah_data(rute):
        page.route = "/tambah-data"
        page.update()
    def go_ubah_data(rute):
        page.route = "/ubah-data"
        page.update()
        
    # Change Route
    def change_route(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[ft.Row(spacing=0,controls=[sidebar,dashboard.my_dashboard.build(dashboard.my_dashboard,width_content)])],
                padding=0,
                spacing=0
            )
        )
        
        if page.route == "/data-siswa":
            page.views.clear()
            page.views.append(
                ft.View(
                    route="/data-siswa",
                    controls=[ft.Row(spacing=0,controls=[sidebar,view_data()])],
                    padding=0,
                    spacing=0
                )
            )
            page.update()
        elif page.route == "/tambah-data":
            page.views.clear()
            page.views.append(
                ft.View(
                    route="/tambah-data",
                    controls=[ft.Row(spacing=0,controls=[sidebar,view_tambah])],
                    padding=0,
                    spacing=0
                )
            )
        elif page.route == "/ubah-data":
            page.views.clear()
            page.views.append(
                ft.View(
                    route="/ubah-data",
                    controls=[ft.Row(spacing=0,controls=[sidebar,view_ubah()])],
                    padding=0,
                    spacing=0
                )
            )
        page.update()
        
    # def sort_data():
    #     sort = False
    #     if sort == False:
                
    
    # SIDEBAR START
    sidebar = ft.Container(bgcolor=ft.colors.with_opacity(0.4,"#BFAC8F"), width=250,height=700,
        content= ft.Column(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,spacing=10,
        controls=[
            # Baris identitas
            ft.Container(margin=ft.margin.only(top=15,left=20,right=20),
                content=ft.Row(spacing=15,
                    controls=[
                        ft.Image(src='assets/image/logo.png', width=70,height=70),
                        ft.Text(
                            "DISK",
                            font_family="FasterOne",
                            size=30,
                            color="#209FBA")
                        ]
                    )
                ),
            
            # baris sidelink
            ft.Container(margin=ft.margin.only(bottom=150,left=20,right=20),
                content=ft.Column(
                    controls=[
                        ft.Container(margin=ft.margin.only(bottom=5),padding=ft.padding.only(bottom=5,top=5,left=5),border_radius=5,on_hover=on_hover,on_click=go_dashboard,
                            content=ft.Row(spacing=20,
                            controls=[
                                ft.Icon(name=ft.icons.DASHBOARD,color="#209FBA"),
                                ft.Text(
                                    "Dashboard",
                                    font_family="PoppinsSemiBold",
                                    size=17,
                                    color="#209FBA")
                                ]
                            )
                        ),
                        ft.Container(margin=ft.margin.only(bottom=10),padding=ft.padding.only(bottom=5,top=5,left=5),border_radius=5,on_hover=on_hover,on_click=go_data,
                            content=ft.Row(spacing=20,
                            controls=[
                                ft.Icon(name="people",color="#209FBA"),
                                ft.Text(
                                    "Data Siswa",
                                    size=17,
                                    font_family="PoppinsSemiBold",
                                    color="#209FBA")
                                ]
                            )
                        ),
                        ft.Container(padding=ft.padding.only(bottom=5,top=5,left=5),border_radius=5,on_hover=on_hover,on_click=go_tentang,
                            content=ft.Row(spacing=20,
                            controls=[
                                ft.Icon(name=ft.icons.INFO,color="#209FBA"),
                                ft.Text(
                                    "Tentang",
                                    size=17,
                                    font_family="PoppinsSemiBold",
                                    color="#209FBA")
                                ]
                            )
                        ),
                    ]
                )
            ),

            # # baris kontrol
            ft.Container(margin=ft.margin.only(left=20,bottom=20,right=20),padding=10,
                content=ft.Column(
                    controls=[
                        ft.Container(margin=ft.margin.only(bottom=10),
                        content=ft.Row(spacing=20,alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[labelMode,
                                ft.Switch(on_change=change_mode,value=False)
                                ]
                            )
                        ),
                        ft.Container(
                        content=ft.Row(spacing=85,
                            controls=[
                                ft.Text(
                                    "Logout",
                                    size=17,
                                    font_family="PoppinsSemiBold",
                                    color="#209FBA"
                                    ),
                                ft.Icon(name='logout',color="#209FBA")
                                ]
                            )
                        )]
                    )
                )           
                ]
            )
        )


    # Tambah Data
    tb_nisn = ft.TextField(height=55,label="NISN")
    tb_nama = ft.TextField(height=55,label="Nama") 
    tb_jenis_kelamin = ft.RadioGroup(content=
                ft.Row(spacing=20,controls=[
                    ft.Radio(value='Laki-Laki', label="Laki-Laki"),
                    ft.Radio(value='Perempuan', label="Perempuan")
                ]
                ))

    tb_kelas = ft.Dropdown(height=55,options=[ft.dropdown.Option("10"),ft.dropdown.Option("11"),ft.dropdown.Option("12")])
    tb_jurusan = ft.Dropdown(height=55,options=[ft.dropdown.Option("TKJ"),ft.dropdown.Option("TPM"),ft.dropdown.Option("DPIB"),ft.dropdown.Option("TKP"),ft.dropdown.Option("TITL"),ft.dropdown.Option("TKR"),ft.dropdown.Option("KI")]) 
        
    def simpan():
        global tabel_data
        nisn = int(tb_nisn.value)
        nama = tb_nama.value
        jenis_kelamin = tb_jenis_kelamin.value
        kelas = tb_kelas.value
        jurusan = tb_jurusan.value
 
        data_handler().tambah_data(nisn,nama,jenis_kelamin,kelas,jurusan)
        tabel_data.clear()
        page.update()
        baca()
        tabel_data = loop(original)
        page.route = "/data-siswa"
        page.update()
        
    view_tambah = ft.Container(width=width_content-500,height=700,padding=15,alignment=ft.alignment.center,
            content=ft.Column(spacing=25,controls=[
                    ft.Row(spacing=0, controls=[
                                ft.Container(margin=5, content= ft.Icon(name="add",size=30,color='#9A0000')),
                                ft.Container(content= ft.Text("Tambah Data", size=33,color='000000',font_family="PoppinsSemiBold",))    
                            ]),
                    tb_nisn,
                    tb_nama,
                    ft.Column(spacing=10,controls=[
                        ft.Text('Jenis Kelamin'),
                        tb_jenis_kelamin
                        ]),
                    tb_kelas,
                    tb_jurusan,
                    ft.Row(spacing=15,controls=[ft.ElevatedButton(text="Kembali",on_click=go_data),ft.FilledButton(text="Simpan",on_click=lambda e:simpan())]),
                    ]
                ),
        )
     
    # Ubah Data
    def view_ubah():
        # for key,index in original.items():
        #     if key == no:
                return ft.Container(width=width_content-500,height=700,padding=15,alignment=ft.alignment.center,
                    content=ft.Column(spacing=25,controls=[
                            ft.Row(spacing=0, controls=[
                                        ft.Container(margin=5, content= ft.Icon(name="edit",size=30,color='#9A0000')),
                                        ft.Container(content= ft.Text("Ubah Data", size=33,color='000000',font_family="PoppinsSemiBold",))    
                                    ]),
                            tb_nisn,
                            tb_nama,
                            ft.Column(spacing=10,controls=[
                                ft.Text('Jenis Kelamin'),
                                tb_jenis_kelamin
                                ]),
                            tb_kelas,
                            tb_jurusan,
                            ft.Row(spacing=15,controls=[ft.ElevatedButton(text="Kembali",on_click=go_data),ft.FilledButton(text="Simpan",on_click=lambda e:simpan())]),
                            ]
                        ),
                )
    
    # Data Siswa
    pencarian = ft.TextField(height=40,border=ft.border.all(1.5,"#74747B"),label="Search...")
    def view_data():
        return ft.Container(content= ft.Container(height=700,width=width_content,bgcolor="#D6E4E5", padding=ft.padding.only(left=15,top=20), 
                          content= ft.Column (spacing=30,alignment=ft.MainAxisAlignment.START, 
            controls=[
                # baris 1
                ft.Row(spacing=8, controls=[
                        ft.Container(margin=5, content=ft.Icon(name="people",size=30,color='#9A0000')),
                        ft.Container(content= ft.Text(
                            "Data Siswa",
                            size=33,
                            font_family="PoppinsSemiBold"
                            ))
                        
                        ]),
                ft.Column(spacing=20,controls=[
                    # baris 2
                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,width=width_content-50,spacing=0,
                        controls=[
                            ft.Container(padding=ft.padding.only(top=8,bottom=8),
                                content=ft.Row(spacing=25,controls=[
                                    ft.Container(content=ft.Row(spacing=8,controls=[pencarian,ft.Icon(name="search")])),
                                    ft.IconButton(
                                        icon=ft.icons.EDIT,
                                        tooltip='Filter Data',
                                        # on_click=sort_data
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.DELETE,
                                        tooltip='Sort',
                                        on_click=lambda e: sort_data
                                    )
                                    ]
                                ),
                            ),
                            ft.Container(
                                content=ft.Row(controls=[ft.Icon(name='add_circle'),ft.Text("Tambah Data",font_family="PoppinsSemiBold")]),
                                on_click = go_tambah_data,
                                alignment=ft.alignment.center,
                                padding=ft.padding.symmetric(horizontal=15),
                                width=170,
                                height=40,
                                border=ft.border.all(1.5,"#74747B"),
                                border_radius=5,
                            )
                        ]
                    ),
                    
                    ft.Container(height=500,width=width_content-50,alignment=ft.alignment.top_center,
                            content=ft.Column(spacing=0,scroll=ft.ScrollMode.AUTO,controls=
                                tabel_data
                        ))
                    ]
                )
            ]
        )
        ))
    
    
    
    # Route  Conf
    page.on_route_change = change_route
    page.go(page.route)
        
# ft.app(target=main,view=ft.AppView.WEB_BROWSER,port=8000)
ft.app(target=main)