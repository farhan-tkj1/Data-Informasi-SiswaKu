import flet as ft

class my_dashboard(ft.UserControl):
    def build(self,width_box):
        return ft.Container(width=width_box,height=700,bgcolor="#909090", padding=ft.padding.only(left=15,top=20,right=15), content= 
                          ft.Column (spacing=0, controls=[

        # baris 1
        ft.Row(spacing=8, controls=[
                ft.Container(margin=5, content= ft.Icon(name="dashboard",size=30,color='#BFAC8F')),
                ft.Container(content= ft.Text(
                    "Dashboard",
                    size=33,
                    color='000000',
                    font_family="PoppinsSemiBold",))
                
                ]),

        # baris 2
        ft.Row(spacing=0, alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[
            ft.Container(
                    content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,spacing=100,controls=[ft.Column(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Text(font_family="PoppinsMedium",size=50,value=100),ft.Text(font_family="PoppinsSemiBold",value="Data Siswa",size=15)]),ft.Image(src='assets/image/logo_people.png',height=80,width=80)]),
                    margin=10,
                    padding=10,
                    bgcolor='#BFAC8F',
                    width = width_box/3 - 40,
                    height=150,
                    border_radius=10,
                ),
            ft.Container(
                    content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,spacing=100,controls=[ft.Column(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Text(font_family="PoppinsSemiBold",value=100,size=50),ft.Text(font_family="PoppinsSemiBold",value="Laki - Laki",size=15)]),ft.Image(src='assets/image/logo_pria.png',height=80,width=80)]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor='#BFAC8F',
                    width = width_box/3 - 40,
                    height=150,
                    border_radius=10,
                ),
            ft.Container(
                    content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,spacing=100,controls=[ft.Column(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Text(font_family="PoppinsSemiBold",value=100,size=50),ft.Text(font_family="PoppinsSemiBold",value="Perempuan",size=15)]),ft.Image(src='assets/image/logo_wanita.png',height=80,width=80)]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor='#BFAC8F',
                    width = width_box/3 - 40,
                    height=150,
                    border_radius=10,
                )]),
           
        # baris 3
        ft.Row(spacing=0, alignment=ft.MainAxisAlignment.SPACE_AROUND, controls=[
            ft.Container(
                    content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[ft.Column(spacing=15,alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Text(font_family="PoppinsMedium",value="KELAS",size=25),ft.Text(font_family="PoppinsSemiBold",value=25,size=15)]),ft.Image(src='assets/image/logo_10.png',height=80,width=80)]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor='#BFAC8F',
                    width= width_box/3 - 40,
                    height=150,
                    border_radius=10,
                ),
            ft.Container(
                    content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,spacing=100,controls=[ft.Column(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Text(font_family="PoppinsSemiBold",value="KELAS",size=25),ft.Text(font_family="PoppinsSemiBold",value=25,size=15)]),ft.Image(src='assets/image/logo_11.png',height=80,width=80)]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor='#BFAC8F',
                    width= width_box/3 - 40,
                    height=150,
                    border_radius=10,
                ),
            ft.Container(
                    content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,spacing=100,controls=[ft.Column(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Text(font_family="PoppinsSemiBold",value="KELAS",size=25),ft.Text(font_family="PoppinsSemiBold",value=25,size=15)]),ft.Image(src='assets/image/logo_12.png',height=80,width=80)]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor='#BFAC8F',
                    width=width_box/3 - 40,
                    height=150,
                    border_radius=10,
                )])
    ]))