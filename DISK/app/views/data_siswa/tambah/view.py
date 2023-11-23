import flet as ft

class tambah_data(ft.UserControl):
    def build(self,width_box):
        tb_nisn = ft.TextField(height=45,label="NISN")
        tb_nama = ft.TextField(height=45,label="NAMA") 
        tb_jenis_kelamin = ft.Column(spacing=10,controls=[
                ft.Text('Jenis Kelamin'),
                ft.Row(spacing=20,controls=[
                    ft.Radio(value='Laki-Laki', label="Laki-Laki"),
                    ft.Radio(value='Perempuan', label="Perempuan")
                        ]
                    )
                ])
        tb_kelas = ft.Dropdown(height=45,options=[ft.dropdown.Option("10"),ft.dropdown.Option("11"),ft.dropdown.Option("12")])
        tb_jurusan = ft.Dropdown(height=45,options=[ft.dropdown.Option("TKJ"),ft.dropdown.Option("TPM"),ft.dropdown.Option("DPIB"),ft.dropdown.Option("TKP"),ft.dropdown.Option("TITL"),ft.dropdown.Option("TKR"),ft.dropdown.Option("KI")]) 
        
        return ft.Container(width=width_box-250,height=700,padding=15,
            content=ft.Column(spacing=25,controls=[
                    ft.Row(spacing=0, controls=[
                                ft.Container(margin=5, content= ft.Icon(name="add", color=ft.colors.BLUE_GREY_500)),
                                ft.Container(content= ft.Text("Tambah Data", size=25))    
                            ]),
                    tb_nisn,
                    tb_nama,
                    tb_jenis_kelamin,
                    tb_kelas,
                    tb_jurusan,
                    ft.Row(spacing=15,controls=[ft.ElevatedButton(text="Kembali",),ft.ElevatedButton(text="Simpan",)]),
                    ]
                ),
        )
        