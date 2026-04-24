import flet as ft
from pages.utils import build_subpage, snack


def build(page: ft.Page, C, go_home, navigate_to):
    c = C()

    actual_f = ft.TextField(
        label="Contraseña actual", password=True, can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
    )
    nueva_f = ft.TextField(
        label="Nueva contraseña", password=True, can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_OPEN,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
    )
    confirmar_f = ft.TextField(
        label="Confirmar nueva contraseña", password=True, can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_RESET,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
    )
    error_t = ft.Text("", color="#F44336", size=13, text_align=ft.TextAlign.CENTER)

    def guardar(e):
        import api_client as api
        error_t.value = ""

        actual = actual_f.value.strip()
        nueva = nueva_f.value.strip()
        confirmar = confirmar_f.value.strip()

        if not actual or not nueva or not confirmar:
            error_t.value = "Completa todos los campos"
            page.update()
            return

        if len(nueva) < 6:
            error_t.value = "La nueva contraseña debe tener al menos 6 caracteres"
            page.update()
            return

        if nueva != confirmar:
            error_t.value = "Las contraseñas no coinciden"
            page.update()
            return

        res = api.cambiar_password(actual, nueva)
        if res["ok"]:
            actual_f.value = ""
            nueva_f.value = ""
            confirmar_f.value = ""
            page.update()
            snack(page, "Contraseña actualizada correctamente ✓")
        else:
            error_t.value = res.get("error", "Error al cambiar contraseña")
            page.update()

    body = [
        ft.Container(
            margin=ft.Margin(16, 0, 16, 0),
            padding=ft.Padding(20, 20, 20, 20),
            border_radius=16, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Column(spacing=14, controls=[
                actual_f,
                nueva_f,
                confirmar_f,
                error_t,
                ft.Container(
                    height=46, border_radius=10, bgcolor=c["ACCENT"],
                    alignment=ft.Alignment(0, 0), on_click=guardar,
                    content=ft.Text("Cambiar contraseña", color="#FFFFFF",
                                    size=14, weight=ft.FontWeight.BOLD),
                ),
            ]),
        ),
    ]

    return build_subpage(page, C, go_home, ft.Icons.LOCK_RESET,
                         "Cambiar contraseña", body)
