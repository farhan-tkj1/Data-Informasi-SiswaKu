from flet import *
from app.views import sidebar
from app.views.dashboard import view_dashboard
from app.views import data_siswa
from app.views.tambah_data import view_tambah_data
from app.views.edit_data import view_edit_data

def main(page : Page):
    page.title = "Data Informasi SiswaKu"
    page.padding = 0
    page.window_height = 740
    page.window_center()
    page.window_resizable = False
    page.window_maximizable  =False
    page.theme_mode = ThemeMode.LIGHT
    page.fonts = {
        "FasterOne" : "app/config/fonts/FasterOne-Regular.ttf",
        "PoppinsSemiBold" : "app/config/fonts/Poppins-SemiBold.ttf",
        "PoppinsSemiBoldItalic" : "app/config/fonts/Poppins-SemiBoldItalic.ttf",
        "PoppinsMedium" : "app/config/fonts/Poppins-Medium.ttf"
    }
    
    def route_change(routes):
        sidebar.view_sidebar(page)
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[Row(spacing=0,controls=[sidebar.view,view_dashboard(page)])],
                padding=0
            )
        )
        page.update()

        if page.route == "/dashboard":
            page.views.append(
                View(
                    route="/dashboard",
                    controls=[Row(spacing=0,controls=[sidebar.view,view_dashboard(page)])],
                    padding=0
                )
            )
            page.update()
            

        elif page.route == "/data-siswa":
            page.views.clear()
            sidebar.view_sidebar(page)
            data_siswa.view_data_siswa(page)
            data_siswa.data(page)
            page.views.append(
                View(
                    route="/data-siswa",
                    controls=[Row(spacing=0,controls=[sidebar.view,Column(height=700,alignment=MainAxisAlignment.SPACE_BETWEEN,spacing=0,controls=[data_siswa.view_data,data_siswa.data_tabel])])],
                    padding=0
                )
            )
            page.update()
            
        elif page.route == "/tambah-data":
            page.views.append(
                View(
                    route="/tambah-data",
                    controls=[Row(spacing=0,controls=[sidebar.view,view_tambah_data(page)])],
                    padding=0
                )
            )
            page.update()
            
            
        elif page.route == "/ubah-data":
            page.views.append(
                View(
                    route="/ubah-data",
                    controls=[Row(spacing=0,controls=[sidebar.view,view_edit_data(page)])],
                    padding=0
                )
            )
            page.update()

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go('/')

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go('/')

    page.update()

app(target = main)  