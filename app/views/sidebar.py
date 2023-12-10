from flet import *

def view_sidebar(page):
    global view
    view = Container(padding=padding.only(bottom=20,left=20,right=20),bgcolor='#DEECFF', width=250,height=700,
            content= Column(alignment=MainAxisAlignment.SPACE_BETWEEN,spacing=10,
                controls=[
                    Container(
                        content=Image(src='app/assets/logo.png', width=200,height=200),
                            ),
                    side_link(page),
                    Container(
                        content=Column(
                            controls=[
                                Container(
                                    content=Row(spacing=25,
                                        controls=[
                                            Stack(
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )

def side_link(page:Page):
    return Column(controls=[
                        Container(margin=margin.only(bottom=5),padding=padding.only(bottom=5,top=5,left=5),border_radius=5,on_click=lambda e: route_to_dashboard(e,page),
                            content=Row(spacing=20,
                                controls=[
                                    Icon(name=icons.DASHBOARD,color="#022E57"),
                                    Text(
                                        "Dashboard",
                                        font_family="PoppinsSemiBold",
                                        size=17,
                                        color="#022E57",   
                                    )
                                ]
                            )
                        ),
                        Container(margin=margin.only(bottom=10),padding=padding.only(bottom=5,top=5,left=5),border_radius=5,on_click=lambda e: route_to_data_siswa(e,page),
                            content=Row(spacing=20,
                                controls=[
                                    Icon(name="people",color="#022E57"),
                                    Text(
                                        "Data Siswa",
                                        size=17,
                                        font_family="PoppinsSemiBold",
                                        color="#022E57",
                                    )
                                ]
                            )
                        ),
                    ]
                )
    
def route_to_dashboard(e,page :Page):
    page.go("/dashboard")
    page.update
    
def route_to_data_siswa(e,page :Page):
    page.go("/data-siswa")
    page.update
    
def route_to_tentang(e,page :Page):
    page.go("/tentang")
    page.update