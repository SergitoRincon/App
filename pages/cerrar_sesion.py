import threading
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

    # Mostrar popup automáticamente al abrir la página
    def mostrar_popup():
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

    threading.Timer(0.2, mostrar_popup).start()

    # Página de fondo simple mientras aparece el popup
    return build_subpage(page, C, go_home, ft.Icons.LOGOUT, "Cerrar sesión", [
        ft.Container(
            margin=ft.Margin(16, 30, 16, 0),
            padding=ft.Padding(24, 32, 24, 32),
            border_radius=16, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12, controls=[
                    ft.Icon(ft.Icons.LOGOUT, color=c["ACCENT"], size=48),
                    ft.Text("Cerrando sesión...", color=c["GRAY"],
                            size=14, text_align=ft.TextAlign.CENTER),
                ],
            ),
        ),
    ])
