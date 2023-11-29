from flet import *
from app.database.data_handler import data_handler

data_siswa = len(data_handler().data_siswa)
siswa_LK = sum(1 for x in data_handler().data_siswa.values() for n in x.values() if n == "Laki-Laki")
siswa_PR = sum(1 for x in data_handler().data_siswa.values() for n in x.values() if n == "Perempuan")
kelas_10 = sum(1 for x in data_handler().data_siswa.values() for n in x.values() if n == "10")
kelas_11 = sum(1 for x in data_handler().data_siswa.values() for n in x.values() if n == "11")
kelas_12 = sum(1 for x in data_handler().data_siswa.values() for n in x.values() if n == "12")

def view_dashboard(page): 
    width_box = page.window_width - 250
    return Container(width=width_box,height=700,bgcolor="#29ADB2",alignment=alignment.center_right,padding=padding.only(left=15,top=20,right=15),
                content=Column(spacing=0,
                    controls=[
                        Row(spacing=8,
                            controls=[
                                Container(margin=5, content= Icon(name="dashboard",size=30,color='#E91E63')),
                                Container(content= Text(
                                    "Dashboard",
                                    size=33,
                                    color='#DEECFF',
                                    font_family="PoppinsSemiBold"
                                    )
                                )
                                
                            ]
                        ),
                        Row(spacing=0, alignment=MainAxisAlignment.SPACE_AROUND,controls=shape_top(page)),
                        Row(spacing=0, alignment=MainAxisAlignment.SPACE_AROUND, controls=shape_bottom(page))
                    ]
                )
            )
    
def shape_top(page):
    width_box = page.window_width - 250
    return [
        Container(
            content=Row(alignment=MainAxisAlignment.SPACE_AROUND,spacing=100,controls=[Column(alignment=MainAxisAlignment.CENTER,controls=[Text(font_family="PoppinsMedium",size=50,value=data_siswa,color='#E91E63'),Text(font_family="PoppinsSemiBold",value="Data Siswa",size=15,color='#022E57')]),Image(src='app/assets/logo_people.png',height=80,width=80)]),
            margin=10,
            padding=10,
            bgcolor='#DEECFF',
            width = width_box/3 - 40,
            height=150,
            border_radius=10,
        ),
        Container(
            content=Row(alignment=MainAxisAlignment.SPACE_AROUND,spacing=100,controls=[Column(alignment=MainAxisAlignment.CENTER,controls=[Text(font_family="PoppinsMedium",size=50,value=siswa_LK,color='#E91E63'),Text(font_family="PoppinsSemiBold",value="Laki - Laki",size=15,color='#022E57')]),Image(src='app/assets/logo_pria.png',height=80,width=80)]),
            margin=10,
            padding=10,
            bgcolor='#DEECFF',
            width = width_box/3 - 40,
            height=150,
            border_radius=10,
        ),
        Container(
            content=Row(alignment=MainAxisAlignment.SPACE_AROUND,spacing=100,controls=[Column(alignment=MainAxisAlignment.CENTER,controls=[Text(font_family="PoppinsMedium",size=50,value=siswa_PR,color='#E91E63'),Text(font_family="PoppinsSemiBold",value="Perempuan",size=15,color='#022E57')]),Image(src='app/assets/logo_wanita.png',height=80,width=80)]),
            margin=10,
            padding=10,
            bgcolor='#DEECFF',
            width = width_box/3 - 40,
            height=150,
            border_radius=10,
        ),
    ]
        
def shape_bottom(page):
    width_box = page.window_width - 250
    return [
        Container(
            content=Row(alignment=MainAxisAlignment.SPACE_AROUND,controls=[Column(spacing=15,alignment=MainAxisAlignment.CENTER,controls=[Text(font_family="PoppinsMedium",value="KELAS",size=25,color='#E91E63'),Text(font_family="PoppinsSemiBold",value=kelas_10,size=15,color='#022E57')]),Image(src='app/assets/logo_10.png',height=80,width=80)]),
            margin=10,
            padding=10,
            alignment=alignment.center,
            bgcolor='#DEECFF',
            width= width_box/3 - 40,
            height=150,
            border_radius=10,
        ),
        Container(
            content=Row(alignment=MainAxisAlignment.SPACE_AROUND,controls=[Column(spacing=15,alignment=MainAxisAlignment.CENTER,controls=[Text(font_family="PoppinsMedium",value="KELAS",size=25,color='#E91E63'),Text(font_family="PoppinsSemiBold",value=kelas_11,size=15,color='#022E57')]),Image(src='app/assets/logo_11.png',height=80,width=80)]),
            margin=10,
            padding=10,
            alignment=alignment.center,
            bgcolor='#DEECFF',
            width= width_box/3 - 40,
            height=150,
            border_radius=10,
        ),
        Container(
            content=Row(alignment=MainAxisAlignment.SPACE_AROUND,controls=[Column(spacing=15,alignment=MainAxisAlignment.CENTER,controls=[Text(font_family="PoppinsMedium",value="KELAS",size=25,color='#E91E63'),Text(font_family="PoppinsSemiBold",value=kelas_12,size=15,color='#022E57')]),Image(src='app/assets/logo_12.png',height=80,width=80)]),
            margin=10,
            padding=10,
            alignment=alignment.center,
            bgcolor='#DEECFF',
            width= width_box/3 - 40,
            height=150,
            border_radius=10,
        ),
    ]