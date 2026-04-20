import flet as ft
from pages.utils import build_subpage, section_title
import api_client as api


def build(page, C, go_home, navigate_to, vehiculo_id_ref):
    c = C()

    prioridad_color = {"Alta": "#F44336", "Media": "#FFC107", "Baja": "#4CAF50"}

    def tarea_row(titulo, desc, nivel):
        return ft.Container(
            margin=ft.Margin(16,0,16,10),
            padding=ft.Padding(16,14,16,14),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(spacing=4, expand=True, controls=[
                        ft.Text(titulo, color=c["WHITE"], size=13,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(desc, color=c["GRAY"], size=11),
                    ]),
                    ft.Container(
                        padding=ft.Padding(8,4,8,4), border_radius=8,
                        bgcolor=prioridad_color.get(nivel, c["ACCENT"]),
                        content=ft.Text(nivel, size=11, color="#FFFFFF"),
                    ),
                ],
            ),
        )

    vid = vehiculo_id_ref[0]
    tareas_alta  = []
    tareas_media = []
    tareas_baja  = []

    if vid:
        res = api.get_mantenimiento(vid)
        if res["ok"]:
            d = res["data"]
            aceite = d.get("aceite", {})
            if aceite.get("km_proximo"):
                tareas_alta.append(("Cambio de aceite",
                                    f"Próximo a los {aceite['km_proximo']} km"))
            cadena = d.get("cadena", {})
            if cadena.get("km_proximo"):
                tareas_media.append(("Revisión de cadena",
                                     f"Próxima a los {cadena['km_proximo']} km"))
            guaya = d.get("guaya_clutch", {})
            if guaya.get("km_proximo_lub"):
                tareas_baja.append(("Lubricar guaya clutch",
                                    f"Próxima a los {guaya['km_proximo_lub']} km"))

    body = []
    if tareas_alta:
        body.append(section_title("ALTA PRIORIDAD", c))
        body.extend([tarea_row(t, d, "Alta") for t, d in tareas_alta])
    if tareas_media:
        body.append(section_title("MEDIA PRIORIDAD", c))
        body.extend([tarea_row(t, d, "Media") for t, d in tareas_media])
    if tareas_baja:
        body.append(section_title("BAJA PRIORIDAD", c))
        body.extend([tarea_row(t, d, "Baja") for t, d in tareas_baja])
    if not (tareas_alta or tareas_media or tareas_baja):
        body.append(ft.Container(
            margin=ft.Margin(16,20,16,20),
            padding=ft.Padding(20,20,20,20),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            alignment=ft.Alignment(0,0),
            content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                              spacing=10, controls=[
                ft.Icon(ft.Icons.CHECK_CIRCLE, color=c["ACCENT"], size=48),
                ft.Text("Todo al día", color=c["WHITE"], size=16,
                        weight=ft.FontWeight.BOLD),
                ft.Text("Completa los módulos de mantenimiento\npara ver alertas aquí.",
                        color=c["GRAY"], size=12, text_align=ft.TextAlign.CENTER),
            ]),
        ))

    return build_subpage(page, C, go_home, ft.Icons.CATEGORY,
                         "Categorías de mantenimiento", body)