import flet as ft
from pages.utils import build_subpage, confirm_dialog, show_loading, hide_loading
import api_client as api


def build(page, C, go_home, navigate_to, on_logout):
    c = C()

    def hacer_logout():
        show_loading(page, "Cerrando sesión...")
        api.cerrar_sesion_local()
        hide_loading(page)
        on_logout()

    def pedir_confirmacion(e):
        confirm_dialog(
            page,
            titulo="¿Cerrar sesión?",
            mensaje="Se cerrará tu sesión actual.\nPodrás volver a ingresar cuando quieras.",
            on_confirm=hacer_logout,
            c=c,
            btn_confirm="Cerrar sesión",
            btn_cancel="Cancelar",
            danger=True,
        )

    return build_subpage(page, C, go_home, ft.Icons.LOGOUT, "Cerrar sesión", [
        ft.Container(
            margin=ft.Margin(16, 20, 16, 20),
            padding=ft.Padding(24, 32, 24, 32),
            border_radius=16, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=16,
                controls=[
                    ft.Icon(ft.Icons.LOGOUT, color=c["ACCENT"], size=56),
                    ft.Text("¿Quieres cerrar sesión?", size=18,
                            weight=ft.FontWeight.BOLD, color=c["WHITE"],
                            text_align=ft.TextAlign.CENTER),
                    ft.Text(
                        "Toca el botón para confirmar.\nPodrás volver a ingresar cuando quieras.",
                        size=13, color=c["GRAY"],
                        text_align=ft.TextAlign.CENTER),
                    ft.Container(height=8),
                    ft.Container(
                        height=46, border_radius=10,
                        bgcolor="#33F44336",
                        border=ft.border.all(1, "#F44336"),
                        alignment=ft.Alignment(0, 0),
                        on_click=pedir_confirmacion,
                        content=ft.Text("Cerrar sesión", color="#F44336",
                                        size=14, weight=ft.FontWeight.BOLD)),
                    ft.Container(
                        height=46, border_radius=10,
                        border=ft.border.all(1, c["BORDER"]),
                        alignment=ft.Alignment(0, 0),
                        on_click=lambda e: go_home(),
                        content=ft.Text("Cancelar", color=c["GRAY"], size=14)),
                ],
            ),
        ),
    ])