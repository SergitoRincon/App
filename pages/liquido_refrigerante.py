import flet as ft
from pages.utils import build_subpage, mostrar_exito, section_title, snack
import api_client as api


def build(page, C, go_home, navigate_to, vehiculo_id_ref):
    c = C()
    es_liquido = [True]

    def mk_tf(label, hint, icon):
        return ft.TextField(label=label, hint_text=hint, prefix_icon=icon,
                            border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                            label_style=ft.TextStyle(color=c["GRAY"]),
                            color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)

    marca_f   = mk_tf("Marca", "Ej: Honda, Motul...", ft.Icons.LABEL)
    ref_f     = mk_tf("Tipo / Referencia", "Ej: OAT, convencional...", ft.Icons.NUMBERS)
    fecha_f   = mk_tf("Último cambio", "DD/MM/AAAA", ft.Icons.CALENDAR_TODAY)
    km_f      = mk_tf("Km en el cambio", "Ej: 8450", ft.Icons.SPEED)
    km_prox_f = mk_tf("Próximo cambio (km)", "Ej: 18450", ft.Icons.UPCOMING)

    liq_col = ft.Column(visible=True, controls=[
        section_title("INFORMACIÓN", c),
        ft.Container(margin=ft.Margin(16,0,16,10), content=marca_f),
        ft.Container(margin=ft.Margin(16,0,16,10), content=ref_f),
        section_title("CAMBIO / REVISIÓN", c),
        ft.Container(margin=ft.Margin(16,0,16,10), content=fecha_f),
        ft.Container(margin=ft.Margin(16,0,16,10), content=km_f),
        ft.Container(margin=ft.Margin(16,0,16,10), content=km_prox_f),
    ])

    aire_msg = ft.Container(
        visible=False,
        margin=ft.Margin(16,10,16,10),
        padding=ft.Padding(20,20,20,20),
        border_radius=12, bgcolor=c["CARD"],
        border=ft.border.all(1, c["BORDER"]),
        alignment=ft.Alignment(0,0),
        content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=10, controls=[
            ft.Icon(ft.Icons.AIR, color=c["ACCENT"], size=40),
            ft.Text("Motor refrigerado por aire", color=c["WHITE"], size=14,
                    text_align=ft.TextAlign.CENTER),
            ft.Text("No aplica líquido refrigerante.", color=c["GRAY"],
                    size=12, text_align=ft.TextAlign.CENTER),
        ]),
    )

    def on_toggle(e):
        es_liquido[0] = e.control.value
        liq_col.visible = es_liquido[0]
        aire_msg.visible = not es_liquido[0]
        page.update()

    def cargar():
        vid = vehiculo_id_ref[0]
        if not vid: return
        res = api.get_mantenimiento(vid)
        if res["ok"]:
            d = res["data"].get("liquido_refrigerante", {})
            marca_f.value   = d.get("marca", "")
            ref_f.value     = d.get("referencia", "")
            fecha_f.value   = d.get("fecha_cambio", "")
            km_f.value      = d.get("km_cambio", "")
            km_prox_f.value = d.get("km_proximo", "")
            es_l = d.get("es_liquido", True)
            es_liquido[0] = es_l
            liq_col.visible = es_l
            aire_msg.visible = not es_l
            page.update()

    def guardar(e):
        vid = vehiculo_id_ref[0]
        if not vid:
            snack(page, "No hay vehículo seleccionado", error=True); return
        datos = {
            "es_liquido": es_liquido[0],
            "marca": marca_f.value or "", "referencia": ref_f.value or "",
            "fecha_cambio": fecha_f.value or "", "km_cambio": km_f.value or "",
            "km_proximo": km_prox_f.value or "",
        }
        res = api.guardar_modulo(vid, "liquido_refrigerante", datos)
        if res["ok"]:
            mostrar_exito(page)
        else:
            snack(page, res.get("error", "Error"), error=True)

    cargar()

    return build_subpage(page, C, go_home, ft.Icons.THERMOSTAT, "Líquido refrigerante", [
        ft.Container(
            margin=ft.Margin(16,0,16,10),
            padding=ft.Padding(16,12,16,12),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(spacing=2, controls=[
                        ft.Text("Motor refrigerado por líquido", color=c["WHITE"], size=14),
                        ft.Text("Desactiva si es refrigerado por aire",
                                color=c["GRAY"], size=11),
                    ]),
                    ft.Switch(value=es_liquido[0], active_color=c["ACCENT"],
                              on_change=on_toggle),
                ],
            ),
        ),
        liq_col,
        aire_msg,
        ft.Container(
            margin=ft.Margin(16,12,16,0), height=46, border_radius=10,
            bgcolor=c["ACCENT"], alignment=ft.Alignment(0,0), on_click=guardar,
            content=ft.Text("Guardar", color="#FFFFFF", size=14,
                            weight=ft.FontWeight.BOLD),
        ),
    ])