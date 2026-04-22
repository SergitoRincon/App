import flet as ft
from pages.utils import build_subpage, section_title, snack, show_loading, hide_loading, mostrar_exito
import api_client as api


def build_mant_page(page, C, go_home, navigate_to,
                    icon, titulo, modulo_key,
                    vehiculo_id_ref: list,
                    field_sections: list):
    c = C()
    all_fields = []
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
                v = datos.get(key)
                if v is not None:
                    widget.value = str(v)
            page.update()

    def guardar(e):
        vid = vehiculo_id_ref[0]
        if not vid:
            snack(page, "No hay vehículo seleccionado", error=True)
            return
        show_loading(page, "Guardando...")
        datos = {key: (widget.value or "") for key, widget in all_fields}
        res = api.guardar_modulo(vid, modulo_key, datos)
        hide_loading(page)
        if res["ok"]:
            mostrar_exito(page)
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