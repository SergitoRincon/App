import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.SETTINGS, "Piñón", [
        section_title("INFORMACIÓN", c),
        text_field("Marca", "Ej: JT, Renthal, Sunstar...", ft.Icons.LABEL, c),
        text_field("Referencia / Número de dientes", "Ej: JTF1590.15", ft.Icons.NUMBERS, c),
        section_title("MANTENIMIENTO", c),
        date_field("Última revisión", c),
        text_field("Kilometraje en revisión", "Ej: 8450", ft.Icons.SPEED, c),
        text_field("Próxima revisión (km)", "Ej: 10000", ft.Icons.UPCOMING, c),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12,
            bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Column(spacing=8, controls=[
                ft.Text("Estado", color=c["GRAY"], size=13),
                ft.Row(spacing=8, controls=[
                    ft.ElevatedButton("Bueno",   bgcolor="#1E4A90D9", color=c["ACCENT"]),
                    ft.ElevatedButton("Regular", bgcolor=c["CARD"],   color=c["GRAY"]),
                    ft.ElevatedButton("Cambiar", bgcolor=c["CARD"],   color=c["GRAY"]),
                ]),
            ]),
        ),
        save_btn(c),
    ])
