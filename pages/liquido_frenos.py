import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.WATER_DROP, "Líquido de frenos", [
        section_title("INFORMACIÓN", c),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            content=ft.Dropdown(
                label="Tipo de líquido",
                options=[
                    ft.dropdown.Option("DOT 3"),
                    ft.dropdown.Option("DOT 4"),
                    ft.dropdown.Option("DOT 5"),
                    ft.dropdown.Option("DOT 5.1"),
                ],
                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                label_style=ft.TextStyle(color=c["GRAY"]),
                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
            ),
        ),
        text_field("Marca", "Ej: Brembo, Motul, ATE...", ft.Icons.LABEL, c),
        section_title("CAMBIO / REVISIÓN", c),
        date_field("Último cambio", c),
        text_field("Kilometraje en el cambio", "Ej: 8450", ft.Icons.SPEED, c),
        text_field("Próximo cambio (km)", "Ej: 18450", ft.Icons.UPCOMING, c),
        save_btn(c),
    ])
