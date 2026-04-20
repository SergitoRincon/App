import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()

    def linea(titulo):
        return [
            section_title(titulo, c),
            ft.Container(
                margin=ft.Margin(16, 0, 16, 10),
                content=ft.Dropdown(
                    label="Tipo de línea",
                    options=[
                        ft.dropdown.Option("Original (caucho)"),
                        ft.dropdown.Option("Acero inoxidable trenzado"),
                        ft.dropdown.Option("Otro"),
                    ],
                    border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                    label_style=ft.TextStyle(color=c["GRAY"]),
                    color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
                ),
            ),
            text_field("Marca", "Ej: Galfer, Brembo...", ft.Icons.LABEL, c),
            date_field("Último cambio / revisión", c),
        ]

    return build_subpage(page, C, go_home, ft.Icons.CABLE, "Líneas de freno y clutch", [
        *linea("LÍNEA FRENO DELANTERO"),
        *linea("LÍNEA FRENO TRASERO"),
        *linea("LÍNEA DE CLUTCH"),
        save_btn(c),
    ])
