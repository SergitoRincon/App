import flet as ft
from pages.utils import build_subpage, info_card, section_title


def build(page, C, go_home, navigate_to):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.MAP, "Mapa", [
        ft.Container(
            margin=ft.Margin(16, 0, 16, 16), height=220, border_radius=14,
            bgcolor=c["CARD"], border=ft.border.all(1, c["BORDER"]),
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER, spacing=8,
                controls=[
                    ft.Icon(ft.Icons.MAP, color=c["ACCENT"], size=52),
                    ft.Text("Mapa próximamente", color=c["GRAY"], size=14),
                    ft.Text("Integración con Google Maps", color=c["GRAY"], size=12),
                ],
            ),
        ),
        section_title("LUGARES CERCANOS", c),
        info_card("Taller más cercano",   "0.8 km — Cl 80 #45", c),
        info_card("Estación de gasolina", "1.2 km — Av 68",     c),
        info_card("Parqueadero de motos", "0.3 km — Cr 15",     c),
        section_title("MI UBICACIÓN", c),
        info_card("Ciudad", "Bogotá, Colombia", c),
        info_card("Zona",   "Norte",            c),
    ])
