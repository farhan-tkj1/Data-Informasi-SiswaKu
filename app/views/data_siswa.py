from flet import *
from app.views.item_tabel import item_tabel
from app.database.manajemen import manajemen_data
from app.views import sidebar

def view_data_siswa(page):
    global FilterKelas,FilterJurusan,view_data,pencarian
    width_box = page.window_width - 250
    pencarian = TextField(on_change=lambda e:search(e,page),height=50,label="Search NISN or Nama",bgcolor='#DEECFF',border_color='#E91E63',label_style=TextStyle(color='#E91E63',font_family="PoppinsMedium"),text_style=TextStyle(color='#E91E63',font_family="PoppinsMedium"))
    
    FilterKelas = Dropdown(value="All",label="Kelas",on_change=lambda e:filter_kelas(e,page),
                           filled=True, color="#29ADB2",bgcolor='#DEECFF',border_color='#E91E63',label_style=TextStyle(color='#E91E63',font_family="PoppinsMedium"),text_style=TextStyle(color='#E91E63',font_family="PoppinsMedium"),width=100,height=50,text_size=15,
                           options=[dropdown.Option("All"),dropdown.Option("10"),dropdown.Option("11"),dropdown.Option("12")])
    
    FilterJurusan = Dropdown(value="All",label="Jurusan",on_change=lambda e:filter_jurusan(e,page),
                             filled=True, color="#29ADB2", bgcolor='#DEECFF',border_color='#E91E63',label_style=TextStyle(color='#E91E63',font_family="PoppinsMedium"),text_style=TextStyle(color='#E91E63',font_family="PoppinsMedium"),width=130,height=50,text_size=15,
                             options=[dropdown.Option("All"),dropdown.Option("TKJ"),dropdown.Option("TPM"),dropdown.Option("DPIB"),dropdown.Option("TKP"),dropdown.Option("TITL"),dropdown.Option("TKR"),dropdown.Option("KI")])
    
    view_data = Container(height=200,width=width_box,bgcolor="#29ADB2", padding=padding.only(left=20,top=20), 
                content= Column (spacing=30,alignment=MainAxisAlignment.START, 
                    controls=[
                        Row(spacing=8,
                            controls=[
                                Container(margin=5, content=Icon(name="people",size=30,color='#E91E63')),
                                Container(content= Text(
                                    "Data Siswa",
                                    color='#DEECFF',
                                    size=33,
                                    font_family="PoppinsSemiBold"
                                    )
                                )
                            ]
                        ),
                        Row(alignment=MainAxisAlignment.SPACE_BETWEEN,width=width_box-50,spacing=0,
                            controls=[
                                Container(padding=padding.only(top=8,bottom=8),
                                    content=Row(spacing=25,controls=[
                                            pencarian,
                                            FilterKelas,
                                            FilterJurusan,
                                            Container(on_click=lambda e:sort(e,page),content=Icon(name='sort_rounded',color="#E91E63",tooltip="Sort"))
                                        ]
                                    ),
                                ),
                                Container(
                                    content=Row(controls=[Icon(name='add_circle',color="#E91E63"),Text("Tambah Data",font_family="PoppinsSemiBold",color="#29ADB2")]),
                                    bgcolor='#DEECFF',
                                    alignment=alignment.center,
                                    padding=padding.symmetric(horizontal=15),
                                    width=170,
                                    height=50,
                                    border=border.all(1.5,"#E91E63"),
                                    border_radius=5,
                                    on_click=lambda e:route_tambah_data(e,page)
                                )
                            ]
                        ),
                    ]
                )
            )

def route_tambah_data(e,page:Page):
    page.go("/tambah-data")
    page.update()
    
def route_edit_data(e,page:Page):
    page.go("/edit-data")
    page.update()

sort_status = False
def data(page):
    global data_tabel,sort_status
    if sort_status:
        if pencarian.value:
            source = manajemen_data().filter(FilterKelas.value,FilterJurusan.value)
            result = manajemen_data().search_data(pencarian.value,source)
        else:
            result = manajemen_data().filter(FilterKelas.value,FilterJurusan.value)
        db = manajemen_data().sort_data(result)
    else:
        if pencarian.value:
            source = manajemen_data().filter(FilterKelas.value,FilterJurusan.value)
            db = manajemen_data().search_data(pencarian.value,source)
        else:
            db = manajemen_data().filter(FilterKelas.value,FilterJurusan.value)
    
    tabel_header = [Row(spacing=0,
                    controls=[
                    Container(border=border.only(top=border.BorderSide(1.3, "#74747B"),right=border.BorderSide(1.3, "#74747B"),bottom=border.BorderSide(1.3, "#74747B"),left=border.BorderSide(1.3, "#74747B")),height=30,width=170,alignment=alignment.center,content=Text(size=15,font_family="PoppinsSemiBold",value='NISN',color='#DEECFF')),
                    Container(border=border.only(top=border.BorderSide(1.3, "#74747B"),right=border.BorderSide(1.3, "#74747B"),bottom=border.BorderSide(1.3, "#74747B")),height=30,width=200,alignment=alignment.center,content=Text(size=15,font_family="PoppinsSemiBold",value='Nama',color='#DEECFF')),
                    Container(border=border.only(top=border.BorderSide(1.3, "#74747B"),right=border.BorderSide(1.3, "#74747B"),bottom=border.BorderSide(1.3, "#74747B")),height=30,width=170,alignment=alignment.center,content=Text(size=15,font_family="PoppinsSemiBold",value='Jenis Kelamin',color='#DEECFF')),
                    Container(border=border.only(top=border.BorderSide(1.3, "#74747B"),right=border.BorderSide(1.3, "#74747B"),bottom=border.BorderSide(1.3, "#74747B")),height=30,width=130,alignment=alignment.center,content=Text(size=15,font_family="PoppinsSemiBold",value='Kelas',color='#DEECFF')),
                    Container(border=border.only(top=border.BorderSide(1.3, "#74747B"),right=border.BorderSide(1.3, "#74747B"),bottom=border.BorderSide(1.3, "#74747B")),height=30,width=130,alignment=alignment.center,content=Text(size=15,font_family="PoppinsSemiBold",value='Jurusan',color='#DEECFF')),
                    Container(border=border.only(top=border.BorderSide(1.3, "#74747B"),right=border.BorderSide(1.3, "#74747B"),bottom=border.BorderSide(1.3, "#74747B")),height=30,width=170,alignment=alignment.center,content=Text(size=15,font_family="PoppinsSemiBold",value='Action',color='#DEECFF'))])]
    error = [Container(alignment=alignment.center,margin=150, width=page.window_width-320,content=Text(font_family="PoppinsSemiBold",size=25, value="Data tidak ada"))]
    data_tabel = Container(width=page.window_width-200,height=700-190,bgcolor="#29ADB2", padding=padding.only(left=20))
    
    if len(db) > 0:
        show_data = [Row(spacing=5,controls=[Text(value="Show",color="#E91E63",font_family="PoppinsSemiBold"),Text(len(db),color="#E91E63",font_family="PoppinsSemiBold"),Text('In',color="#E91E63",font_family="PoppinsSemiBold"),Text(len(manajemen_data().data_original),color="#E91E63",font_family="PoppinsSemiBold"),Text('Data',color="#E91E63",font_family="PoppinsSemiBold")])]
        tabel_data = [item_tabel(key,index['Nama'],index['Jenis Kelamin'],index['Kelas'],index['Jurusan'],page) for key,index in db.items()]
        data_tabel.content = ListView(spacing=0,controls=show_data + tabel_header + tabel_data)
    else:
        data_tabel.content = Column(spacing=0,scroll=ScrollMode.AUTO,controls=tabel_header + error)

def filter_kelas(e,page:Page):
    data(page)
    page.views[0].controls = [Row(spacing=0,controls=[sidebar.view,Column(height=700,alignment=MainAxisAlignment.SPACE_BETWEEN,spacing=0,controls=[view_data,data_tabel])])]
    page.update()
    
def filter_jurusan(e,page:Page):
    data(page)
    page.views[0].controls = [Row(spacing=0,controls=[sidebar.view,Column(height=700,alignment=MainAxisAlignment.SPACE_BETWEEN,spacing=0,controls=[view_data,data_tabel])])]
    page.update()
    
def search(e,page:Page):
    if pencarian.value:
        pencarian.autofocus = True
    else:
        pencarian.autofocus = False
    data(page)
    page.views[0].controls = [Row(spacing=0,controls=[sidebar.view,Column(height=700,alignment=MainAxisAlignment.SPACE_BETWEEN,spacing=0,controls=[view_data,data_tabel])])]
    page.update()
    
def sort(e,page:Page):
    global sort_status
    if sort_status:
        sort_status = False
    else:
        sort_status = True
    data(page)
    page.views[0].controls = [Row(spacing=0,controls=[sidebar.view,Column(height=700,alignment=MainAxisAlignment.SPACE_BETWEEN,spacing=0,controls=[view_data,data_tabel])])]
    page.update()