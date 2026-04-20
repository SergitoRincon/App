import flet as ft
from pages.utils import build_subpage, section_title, snack, show_loading, hide_loading
import api_client as api


def build(page, C, go_home, navigate_to, usuario_data: dict):
    c = C()

    nombre_f = ft.TextField(
        label="Nombre completo",
        value=usuario_data.get("nombre", ""),
        prefix_icon=ft.Icons.PERSON,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)

    email_val = usuario_data.get("email", "")
    desde_val = usuario_data.get("creado_en", "")[:10] if usuario_data.get("creado_en") else ""

    def guardar(e):
        nuevo_nombre = nombre_f.value.strip()
        if not nuevo_nombre:
            snack(page, "El nombre no puede estar vacío", error=True)
            return
        show_loading(page, "Guardando...")
        res = api.actualizar_perfil({"nombre": nuevo_nombre})
        hide_loading(page)
        if res["ok"]:
            usuario_data["nombre"] = nuevo_nombre
            snack(page, "Perfil actualizado ✓")
        else:
            snack(page, res.get("error", "Error al guardar"), error=True)

    return build_subpage(page, C, go_home, ft.Icons.PERSON, "Mi perfil", [
        # Avatar
        ft.Container(
            alignment=ft.Alignment(0, 0),
            margin=ft.Margin(0, 10, 0, 20),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
                controls=[
                    ft.Container(
                        width=90, height=90, border_radius=45,
                        bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
                        content=ft.Icon(ft.Icons.PERSON,
                                        color="#FFFFFF", size=48),
                    ),
                    ft.Text(usuario_data.get("nombre", ""),
                            size=18, weight=ft.FontWeight.BOLD,
                            color=c["WHITE"]),
                    ft.Text(email_val, size=12, color=c["GRAY"]),
                ],
            ),
        ),
        section_title("EDITAR PERFIL", c),
        ft.Container(margin=ft.Margin(16, 0, 16, 10), content=nombre_f),
        # Email (no editable)
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text("Correo", color=c["GRAY"], size=13),
                    ft.Text(email_val, color=c["WHITE"], size=13,
                            weight=ft.FontWeight.BOLD),
                ],
            ),
        ),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text("Miembro desde", color=c["GRAY"], size=13),
                    ft.Text(desde_val, color=c["WHITE"], size=13,
                            weight=ft.FontWeight.BOLD),
                ],
            ),
        ),
        ft.Container(
            margin=ft.Margin(16, 8, 16, 0),
            height=46, border_radius=10,
            bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
            on_click=guardar,
            content=ft.Text("Guardar cambios", color="#FFFFFF",
                            size=14, weight=ft.FontWeight.BOLD),
        ),
    ])