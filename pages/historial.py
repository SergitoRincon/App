import flet as ft
from pages.utils import build_subpage, section_title
from pages.utils import nivel_color


def build(page, C, go_home, navigate_to):
    c = C()

    def historial_row(fecha, evento, icono, color_ic):
        return ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=12,
                controls=[
                    ft.Container(width=38, height=38, border_radius=19,
                                 bgcolor="#1E4A90D9", alignment=ft.Alignment(0, 0),
                                 content=ft.Icon(icono, color=color_ic, size=18)),
                    ft.Column(spacing=4, expand=True, controls=[
                        ft.Text(evento, color=c["WHITE"], size=13,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(fecha,  color=c["GRAY"],  size=11),
                    ]),
                ],
            ),
        )

    return build_subpage(page, C, go_home, ft.Icons.HISTORY, "Historial", [
        section_title("ENERO 2025", c),
        historial_row("22 Ene", "Carga de combustible — 10L",
                      ft.Icons.LOCAL_GAS_STATION, nivel_color(60)),
        historial_row("15 Ene", "Cambio de aceite — Taller Benelli",
                      ft.Icons.OIL_BARREL, c["ACCENT"]),
        historial_row("10 Ene", "Tensión cadena",
                      ft.Icons.LINK, nivel_color(80)),
        section_title("DICIEMBRE 2024", c),
        historial_row("28 Dic", "Renovación SOAT",
                      ft.Icons.DESCRIPTION, nivel_color(100)),
        historial_row("15 Dic", "Cambio de llantas",
                      ft.Icons.TIRE_REPAIR, c["ACCENT"]),
        historial_row("05 Dic", "Cambio de bujía",
                      ft.Icons.BOLT, c["ACCENT"]),
    ])
