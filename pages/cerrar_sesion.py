import flet as ft
from pages.utils import build_subpage
import api_client as api


def build(page, C, go_home, navigate_to, on_logout):
    c = C()

    def confirmar(e):
        api.cerrar_sesion_local()
        on_logout()

    return build_subpage(page, C, go_home, ft.Icons.LOGOUT, "Cerrar sesión", [
        ft.Container(
            margin=ft.Margin(16, 20, 16, 20),
            padding=ft.Padding(24, 24, 24, 24),
            border_radius=16, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=16,
                controls=[
                    ft.Icon(ft.Icons.LOGOUT, color=c["ACCENT"], size=56),
                    ft.Text("¿Cerrar sesión?", size=20,
                            weight=ft.FontWeight.BOLD, color=c["WHITE"]),
                    ft.Text(
                        "Se cerrará tu sesión.\nPodrás volver a ingresar cuando quieras.",
                        size=13, color=c["GRAY"],
                        text_align=ft.TextAlign.CENTER),
                    ft.Container(
                        width=220, height=46, border_radius=10,
                        bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
                        on_click=confirmar,
                        content=ft.Text("Confirmar", color="#FFFFFF",
                                        size=14, weight=ft.FontWeight.BOLD)),
                    ft.Container(
                        width=220, height=46, border_radius=10,
                        border=ft.border.all(1, c["BORDER"]),
                        alignment=ft.Alignment(0, 0),
                        on_click=lambda e: go_home(),
                        content=ft.Text("Cancelar", color=c["GRAY"], size=14)),
                ],
            ),
        ),
    ])
