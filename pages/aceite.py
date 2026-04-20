import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.OIL_BARREL, "Aceite", [
        section_title("INFORMACIÓN DEL ACEITE", c),
        text_field("Marca del aceite", "Ej: Castrol, Mobil, Shell...", ft.Icons.LABEL, c),
        text_field("Referencia", "Ej: 10W40, 20W50...", ft.Icons.NUMBERS, c),
        section_title("CAMBIO DE ACEITE", c),
        date_field("Fecha del último cambio", c),
        text_field("Kilometraje en el cambio", "Ej: 8450", ft.Icons.SPEED, c),
        text_field("Próximo cambio (km)", "Ej: 9450", ft.Icons.UPCOMING, c),
        section_title("NIVEL DE ACEITE", c),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12,
            bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Column(spacing=10, controls=[
                ft.Text("Nivel actual", color=c["GRAY"], size=13),
                ft.Slider(min=0, max=100, value=80,
                          active_color=c["ACCENT"], inactive_color=c["BAR"],
                          divisions=4, label="{value}%"),
                ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                    ft.Text("Bajo",   color=c["GRAY"], size=11),
                    ft.Text("Normal", color=c["GRAY"], size=11),
                    ft.Text("Alto",   color=c["GRAY"], size=11),
                ]),
            ]),
        ),
        save_btn(c),
    ])
