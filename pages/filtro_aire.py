import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    bg = "#2C2C2C" if page.platform_brightness == ft.Brightness.DARK else "#FFFFFF"
    return build_subpage(page, C, go_home, ft.Icons.AIR, "Filtro de aire", [
        section_title("INFORMACIÓN DEL FILTRO", c),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            content=ft.Dropdown(
                label="Tipo de filtro",
                options=[
                    ft.dropdown.Option("Papel"),
                    ft.dropdown.Option("Espuma"),
                    ft.dropdown.Option("Algodón (K&N)"),
                    ft.dropdown.Option("Otro"),
                ],
                border_color=c["BORDER"],
                focused_border_color=c["ACCENT"],
                label_style=ft.TextStyle(color=c["GRAY"]),
                color=c["WHITE"],
                bgcolor=c["CARD"],
                border_radius=10,
            ),
        ),
        text_field("Marca", "Ej: K&N, Mann, Fram...", ft.Icons.LABEL, c),
        section_title("MANTENIMIENTO", c),
        date_field("Último cambio", c),
        date_field("Última revisión", c),
        text_field("Kilometraje en último cambio", "Ej: 8450", ft.Icons.SPEED, c),
        text_field("Próximo cambio (km)", "Ej: 10450", ft.Icons.UPCOMING, c),
        save_btn(c),
    ])
