import flet as ft
from pages.utils import build_subpage, section_title


def build(page, C, go_home, navigate_to, PLACAS_MENU):
    c = C()

    def vehiculo_card(placa, marca, modelo, anio, activo=False):
        return ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12,
            bgcolor=c["CARD"],
            border=ft.border.all(2 if activo else 1,
                                  c["ACCENT"] if activo else c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(spacing=4, controls=[
                        ft.Text(placa, size=16, weight=ft.FontWeight.BOLD, color=c["WHITE"]),
                        ft.Text(f"{marca} {modelo}, {anio}", size=12, color=c["GRAY"]),
                    ]),
                    ft.Container(
                        padding=ft.Padding(8, 4, 8, 4), border_radius=8,
                        bgcolor=c["ACCENT"] if activo else ft.Colors.TRANSPARENT,
                        content=ft.Text("Activo" if activo else "Inactivo",
                                        size=11, color="#FFFFFF" if activo else c["GRAY"]),
                    ),
                ],
            ),
        )

    return build_subpage(page, C, go_home, ft.Icons.TWO_WHEELER, "Mis vehículos", [
        section_title("MIS VEHÍCULOS", c),
        vehiculo_card("DUW79G", "Benelli", "180s",  "2022", activo=True),
        vehiculo_card("JHR45L", "Honda",   "CB125", "2020"),
        ft.Container(
            margin=ft.Margin(16, 6, 16, 0),
            padding=ft.Padding(0, 12, 0, 12),
            border_radius=12,
            border=ft.border.all(1, c["ACCENT"]),
            bgcolor=ft.Colors.TRANSPARENT,
            alignment=ft.Alignment(0, 0),
            content=ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.Icon(ft.Icons.ADD, color=c["ACCENT"], size=18),
                ft.Container(width=6),
                ft.Text("Agregar vehículo", color=c["ACCENT"], size=14),
            ]),
        ),
    ])
