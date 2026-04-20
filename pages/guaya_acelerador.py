import flet as ft
from pages.utils import build_subpage, section_title, snack
import api_client as api


def build(page, C, go_home, navigate_to, vehiculo_id_ref):
    c = C()
    es_guaya = [True]

    def mk_tf(label, hint, icon):
        return ft.TextField(
            label=label, hint_text=hint, prefix_icon=icon,
            border_color=c["BORDER"], focused_border_color=c["ACCENT"],
            label_style=ft.TextStyle(color=c["GRAY"]),
            color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)

    fecha_lub_f   = mk_tf("Última lubricación", "DD/MM/AAAA", ft.Icons.CALENDAR_TODAY)
    producto_f    = mk_tf("Producto usado", "Ej: WD-40...", ft.Icons.LABEL)
    km_lub_f      = mk_tf("Próxima lubricación (km)", "Ej: 9000", ft.Icons.UPCOMING)
    fecha_camb_f  = mk_tf("Último cambio", "DD/MM/AAAA", ft.Icons.CALENDAR_TODAY)
    km_proximo_f  = mk_tf("Próximo cambio (km)", "Ej: 18450", ft.Icons.UPCOMING)

    all_fields = [
        ("fecha_lubricacion", fecha_lub_f),
        ("producto_lubricacion", producto_f),
        ("km_proximo_lubricacion", km_lub_f),
        ("fecha_cambio", fecha_camb_f),
        ("km_proximo_cambio", km_proximo_f),
        ("es_guaya", None),
    ]

    guaya_col = ft.Column(visible=True, controls=[
        section_title("LUBRICACIÓN", c),
        ft.Container(margin=ft.Margin(16,0,16,10), content=fecha_lub_f),
        ft.Container(margin=ft.Margin(16,0,16,10), content=producto_f),
        ft.Container(margin=ft.Margin(16,0,16,10), content=km_lub_f),
        section_title("CAMBIO", c),
        ft.Container(margin=ft.Margin(16,0,16,10), content=fecha_camb_f),
        ft.Container(margin=ft.Margin(16,0,16,10), content=km_proximo_f),
    ])

    electro_msg = ft.Container(
        visible=False,
        margin=ft.Margin(16,10,16,10),
        padding=ft.Padding(20,20,20,20),
        border_radius=12, bgcolor=c["CARD"],
        border=ft.border.all(1, c["BORDER"]),
        alignment=ft.Alignment(0,0),
        content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=10, controls=[
            ft.Icon(ft.Icons.ELECTRIC_BOLT, color=c["ACCENT"], size=40),
            ft.Text("Acelerador electrónico (TbW)", color=c["WHITE"],
                    size=14, text_align=ft.TextAlign.CENTER),
            ft.Text("No requiere lubricación de guaya.",
                    color=c["GRAY"], size=12, text_align=ft.TextAlign.CENTER),
        ]),
    )

    def on_toggle(e):
        es_guaya[0] = e.control.value
        guaya_col.visible  = es_guaya[0]
        electro_msg.visible = not es_guaya[0]
        page.update()

    def cargar():
        vid = vehiculo_id_ref[0]
        if not vid: return
        res = api.get_mantenimiento(vid)
        if res["ok"]:
            d = res["data"].get("guaya_acelerador", {})
            fecha_lub_f.value  = d.get("fecha_lubricacion", "")
            producto_f.value   = d.get("producto_lubricacion", "")
            km_lub_f.value     = d.get("km_proximo_lubricacion", "")
            fecha_camb_f.value = d.get("fecha_cambio", "")
            km_proximo_f.value = d.get("km_proximo_cambio", "")
            es_g = d.get("es_guaya", True)
            es_guaya[0] = es_g
            guaya_col.visible  = es_g
            electro_msg.visible = not es_g
            page.update()

    def guardar(e):
        vid = vehiculo_id_ref[0]
        if not vid:
            snack(page, "No hay vehículo seleccionado", error=True); return
        datos = {
            "es_guaya": es_guaya[0],
            "fecha_lubricacion": fecha_lub_f.value or "",
            "producto_lubricacion": producto_f.value or "",
            "km_proximo_lubricacion": km_lub_f.value or "",
            "fecha_cambio": fecha_camb_f.value or "",
            "km_proximo_cambio": km_proximo_f.value or "",
        }
        res = api.guardar_modulo(vid, "guaya_acelerador", datos)
        if res["ok"]:
            snack(page, "Guardado correctamente ✓")
        else:
            snack(page, res.get("error", "Error"), error=True)

    cargar()

    return build_subpage(page, C, go_home, ft.Icons.CABLE, "Guaya de acelerador", [
        section_title("TIPO DE ACELERADOR", c),
        ft.Container(
            margin=ft.Margin(16,0,16,10),
            padding=ft.Padding(16,12,16,12),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(spacing=2, controls=[
                        ft.Text("Acelerador por guaya", color=c["WHITE"], size=14),
                        ft.Text("Desactiva si es electrónico (TbW)",
                                color=c["GRAY"], size=11),
                    ]),
                    ft.Switch(value=es_guaya[0], active_color=c["ACCENT"],
                              on_change=on_toggle),
                ],
            ),
        ),
        guaya_col,
        electro_msg,
        ft.Container(
            margin=ft.Margin(16,12,16,0), height=46, border_radius=10,
            bgcolor=c["ACCENT"], alignment=ft.Alignment(0,0), on_click=guardar,
            content=ft.Text("Guardar", color="#FFFFFF", size=14,
                            weight=ft.FontWeight.BOLD),
        ),
    ])
