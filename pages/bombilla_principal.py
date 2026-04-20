import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.LIGHT_MODE, "Bombilla principal", [
        section_title("INFORMACIÓN", c),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            content=ft.Dropdown(
                label="Tipo de bombilla",
                options=[
                    ft.dropdown.Option("Halógena"),
                    ft.dropdown.Option("LED"),
                    ft.dropdown.Option("HID / Xenón"),
                    ft.dropdown.Option("Incandescente"),
                ],
                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                label_style=ft.TextStyle(color=c["GRAY"]),
                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
            ),
        ),
        text_field("Marca", "Ej: Philips, Osram, Bosch...", ft.Icons.LABEL, c),
        text_field("Referencia / Potencia", "Ej: H4 60/55W...", ft.Icons.NUMBERS, c),
        section_title("CAMBIO / REVISIÓN", c),
        date_field("Último cambio", c),
        text_field("Próximo cambio estimado", "Ej: 2026", ft.Icons.UPCOMING, c),
        save_btn(c),
    ])
