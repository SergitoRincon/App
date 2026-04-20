import flet as ft
from pages.utils import build_subpage, info_card, section_title


def build(page, C, go_home, navigate_to, USUARIO, PLACA, MARCA, MODELO, ANIO):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.PERSON, "Mi perfil", [
        ft.Container(
            alignment=ft.Alignment(0, 0),
            margin=ft.Margin(0, 10, 0, 20),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=90, height=90, border_radius=45,
                        bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
                        content=ft.Icon(ft.Icons.PERSON, color="#FFFFFF", size=48),
                    ),
                    ft.Container(height=10),
                    ft.Text(USUARIO, size=22, weight=ft.FontWeight.BOLD, color=c["WHITE"]),
                    ft.Text("Usuario MotoApp", size=13, color=c["GRAY"]),
                ],
            ),
        ),
        section_title("INFORMACIÓN PERSONAL", c),
        info_card("Nombre",    USUARIO,             c),
        info_card("Vehículo",  f"{MARCA} {MODELO}", c),
        info_card("Placa",     PLACA,               c),
        info_card("Año",       ANIO,                c),
        section_title("CUENTA", c),
        info_card("Correo",        "usuario@email.com", c),
        info_card("Miembro desde", "2024",              c),
    ])
