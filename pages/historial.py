import flet as ft
from pages.utils import build_subpage, section_title
import api_client as api


def build(page, C, go_home, navigate_to, vehiculo_id_ref=None):
    c = C()

    vid = vehiculo_id_ref[0] if vehiculo_id_ref else None
    eventos = []

    if vid:
        res = api.get_historial(vid)
        if res["ok"]:
            eventos = res["data"]

    def evento_row(ev):
        fecha = ev.get("fecha_evento", "")[:10]
        return ft.Container(
            margin=ft.Margin(16,0,16,10),
            padding=ft.Padding(16,14,16,14),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=12,
                controls=[
                    ft.Container(
                        width=38, height=38, border_radius=19,
                        bgcolor="#1E4A90D9", alignment=ft.Alignment(0,0),
                        content=ft.Icon(ft.Icons.HISTORY, color=c["ACCENT"], size=18),
                    ),
                    ft.Column(spacing=4, expand=True, controls=[
                        ft.Text(ev.get("titulo",""), color=c["WHITE"], size=13,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(fecha, color=c["GRAY"], size=11),
                    ]),
                ],
            ),
        )

    body = []
    if eventos:
        body.append(section_title(f"{len(eventos)} EVENTOS REGISTRADOS", c))
        body.extend([evento_row(ev) for ev in eventos])
    else:
        body.append(ft.Container(
            margin=ft.Margin(16,30,16,30),
            padding=ft.Padding(20,30,20,30),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            alignment=ft.Alignment(0,0),
            content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                              spacing=10, controls=[
                ft.Icon(ft.Icons.HISTORY, color=c["ACCENT"], size=48),
                ft.Text("Sin historial aún", color=c["WHITE"], size=16,
                        weight=ft.FontWeight.BOLD),
                ft.Text("Los cambios que guardes\naparecerán aquí.",
                        color=c["GRAY"], size=12, text_align=ft.TextAlign.CENTER),
            ]),
        ))

    return build_subpage(page, C, go_home, ft.Icons.HISTORY, "Historial", body)
