"""
Utilidad para páginas de mantenimiento que guardan/cargan desde la API.
Cada página usa build_mant_page() pasando sus campos.
"""
import flet as ft
from pages.utils import build_subpage, section_title, snack
import api_client as api


def text_f(label, hint, icon, c, ref):
    tf = ft.TextField(
        label=label, hint_text=hint,
        prefix_icon=icon,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
    )
    ref.append(tf)
    return ft.Container(margin=ft.Margin(16, 0, 16, 10), content=tf)


def date_f(label, c, ref):
    return text_f(label, "DD/MM/AAAA", ft.Icons.CALENDAR_TODAY, c, ref)


def km_f(label, c, ref):
    return text_f(label, "Ej: 8450", ft.Icons.SPEED, c, ref)


def dropdown_f(label, options, c, ref):
    dd = ft.Dropdown(
        label=label,
        options=[ft.dropdown.Option(o) for o in options],
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
    )
    ref.append(dd)
    return ft.Container(margin=ft.Margin(16, 0, 16, 10), content=dd)


def build_mant_page(page, C, go_home, navigate_to,
                    icon, titulo, modulo_key,
                    vehiculo_id_ref: list,
                    field_sections: list):
    """
    field_sections: lista de tuplas (seccion_titulo, [controles])
    Los controles son widgets ft.* con un atributo .value para guardar/cargar.
    field_sections también incluye las refs de los fields para guardar.
    """
    c = C()

    # Recopilar todos los fields con sus keys
    all_fields = []   # lista de (key, widget)
    body = []

    for sec_title, fields_with_keys in field_sections:
        body.append(section_title(sec_title, c))
        for key, widget in fields_with_keys:
            all_fields.append((key, widget))
            body.append(ft.Container(margin=ft.Margin(16, 0, 16, 10),
                                      content=widget))

    def cargar():
        vid = vehiculo_id_ref[0]
        if not vid:
            return
        res = api.get_mantenimiento(vid)
        if res["ok"]:
            datos = res["data"].get(modulo_key, {})
            for key, widget in all_fields:
                if key in datos and datos[key] is not None:
                    widget.value = str(datos[key])
            page.update()

    def guardar(e):
        vid = vehiculo_id_ref[0]
        if not vid:
            snack(page, "No hay vehículo seleccionado", error=True)
            return
        datos = {key: widget.value or "" for key, widget in all_fields}
        res = api.guardar_modulo(vid, modulo_key, datos)
        if res["ok"]:
            snack(page, "Guardado correctamente ✓")
        else:
            snack(page, res.get("error", "Error al guardar"), error=True)

    cargar()

    body.append(
        ft.Container(
            margin=ft.Margin(16, 12, 16, 0),
            height=46, border_radius=10,
            bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
            on_click=guardar,
            content=ft.Text("Guardar", color="#FFFFFF", size=14,
                            weight=ft.FontWeight.BOLD),
        )
    )

    return build_subpage(page, C, go_home, icon, titulo, body)
