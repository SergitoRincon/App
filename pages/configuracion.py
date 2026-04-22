import flet as ft
from pages.utils import build_subpage, mostrar_exito, section_title, snack
import api_client as api


def build(page, C, go_home, navigate_to):
    c = C()
    cfg_data = {}

    def cargar():
        res = api.get_configuracion()
        if res["ok"]:
            cfg_data.update(res["data"])
            _render()

    def guardar(key, value):
        res = api.actualizar_configuracion({key: value})
        if res["ok"]:
            snack(page, "Guardado ✓")
        else:
            snack(page, res.get("error", "Error"), error=True)

    def toggle_row(label, subtitle, key):
        val = cfg_data.get(key, False)
        def on_change(e, k=key):
            guardar(k, e.control.value)
        return ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(spacing=2, controls=[
                        ft.Text(label, color=c["WHITE"], size=14),
                        ft.Text(subtitle, color=c["GRAY"], size=11),
                    ]),
                    ft.Switch(value=val, active_color=c["ACCENT"],
                              on_change=on_change),
                ],
            ),
        )

    col = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def _render():
        col.controls = [
            ft.Container(height=16),
            section_title("NOTIFICACIONES", c),
            toggle_row("Alertas de mantenimiento",
                       "Recibe alertas sobre servicios próximos",
                       "alertas_mantenimiento"),
            toggle_row("Recordatorios de combustible",
                       "Aviso cuando el nivel baja",
                       "alertas_combustible"),
            toggle_row("Alertas de documentos",
                       "Documentos próximos a vencer",
                       "alertas_documentos"),
            section_title("PRIVACIDAD", c),
            toggle_row("Compartir ubicación",
                       "Para mostrar talleres cercanos",
                       "compartir_ubicacion"),
            ft.Container(height=20),
        ]
        page.update()

    cargar()

    header = ft.Container(
        bgcolor=c["CARD"],
        border=ft.border.only(bottom=ft.BorderSide(1, c["BORDER"])),
        padding=ft.Padding(10, 12, 16, 12),
        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=40, height=40, border_radius=20,
                    bgcolor=ft.Colors.TRANSPARENT,
                    alignment=ft.Alignment(0, 0),
                    on_hover=lambda e: (
                        setattr(e.control, "bgcolor",
                                "#1E4A90D9" if e.data == "true" else ft.Colors.TRANSPARENT),
                        page.update()),
                    on_click=lambda e: go_home(),
                    content=ft.Icon(ft.Icons.ARROW_BACK_IOS_NEW,
                                    color=c["ACCENT"], size=20),
                ),
                ft.Container(width=8),
                ft.Icon(ft.Icons.SETTINGS, color=c["ACCENT"], size=26),
                ft.Container(width=8),
                ft.Text("Configuración", size=20,
                        weight=ft.FontWeight.BOLD, color=c["WHITE"]),
            ],
        ),
    )
    col.controls.insert(0, header)
    return col