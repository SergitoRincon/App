import flet as ft
from pages.utils import build_subpage, section_title, snack
import api_client as api


def build(page, C, go_home, navigate_to, vehiculo_actual_id: list,
          on_vehiculo_cambiado=None):
    c = C()
    vehiculos_data = []
    loading = ft.ProgressRing(width=22, height=22, color=c["ACCENT"])
    lista   = ft.Column(tight=True, spacing=0)

    # Campos para agregar vehículo
    placa_f  = ft.TextField(label="Placa",  hint_text="Ej: DUW79G",
                             border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                             label_style=ft.TextStyle(color=c["GRAY"]),
                             color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)
    marca_f  = ft.TextField(label="Marca",  hint_text="Ej: Benelli",
                             border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                             label_style=ft.TextStyle(color=c["GRAY"]),
                             color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)
    modelo_f = ft.TextField(label="Modelo", hint_text="Ej: 180s",
                             border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                             label_style=ft.TextStyle(color=c["GRAY"]),
                             color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)
    anio_f   = ft.TextField(label="Año",    hint_text="Ej: 2022",
                             keyboard_type=ft.KeyboardType.NUMBER,
                             border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                             label_style=ft.TextStyle(color=c["GRAY"]),
                             color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)
    form_visible = ft.Ref[ft.Container]()

    def cargar():
        res = api.get_vehiculos()
        if res["ok"]:
            vehiculos_data.clear()
            vehiculos_data.extend(res["data"])
            _render_lista()
        else:
            snack(page, res.get("error", "Error al cargar"), error=True)

    def _render_lista():
        lista.controls.clear()
        if not vehiculos_data:
            lista.controls.append(
                ft.Container(
                    margin=ft.Margin(16, 10, 16, 10),
                    padding=ft.Padding(20, 20, 20, 20),
                    border_radius=12, bgcolor=c["CARD"],
                    border=ft.border.all(1, c["BORDER"]),
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text("No tienes vehículos registrados",
                                    color=c["GRAY"], size=13,
                                    text_align=ft.TextAlign.CENTER),
                )
            )
        for v in vehiculos_data:
            activo = v["id"] == vehiculo_actual_id[0]
            def _seleccionar(e, vid=v["id"]):
                vehiculo_actual_id[0] = vid
                if on_vehiculo_cambiado:
                    on_vehiculo_cambiado(vid)
                go_home()

            def _eliminar(e, vid=v["id"]):
                res = api.eliminar_vehiculo(vid)
                if res["ok"]:
                    if vehiculo_actual_id[0] == vid:
                        vehiculo_actual_id[0] = None
                    snack(page, "Vehículo eliminado")
                    cargar()
                else:
                    snack(page, res.get("error", "Error"), error=True)

            lista.controls.append(
                ft.Container(
                    margin=ft.Margin(16, 0, 16, 10),
                    padding=ft.Padding(16, 14, 16, 14),
                    border_radius=12, bgcolor=c["CARD"],
                    border=ft.border.all(2 if activo else 1,
                                          c["ACCENT"] if activo else c["BORDER"]),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Column(spacing=4, expand=True, controls=[
                                ft.Text(v["placa"], size=16,
                                        weight=ft.FontWeight.BOLD, color=c["WHITE"]),
                                ft.Text(f"{v['marca']} {v['modelo']}, {v['anio']}",
                                        size=12, color=c["GRAY"]),
                            ]),
                            ft.Row(spacing=8, controls=[
                                ft.Container(
                                    padding=ft.Padding(10, 6, 10, 6),
                                    border_radius=8,
                                    bgcolor=c["ACCENT"] if activo else "#1E4A90D9",
                                    on_click=_seleccionar,
                                    content=ft.Text(
                                        "Activo" if activo else "Usar",
                                        size=11,
                                        color="#FFFFFF"),
                                ),
                                ft.Container(
                                    padding=ft.Padding(10, 6, 10, 6),
                                    border_radius=8,
                                    bgcolor="#33F44336",
                                    on_click=_eliminar,
                                    content=ft.Icon(ft.Icons.DELETE_OUTLINE,
                                                    color="#F44336", size=16),
                                ),
                            ]),
                        ],
                    ),
                )
            )
        page.update()

    def agregar(e):
        if not placa_f.value or not marca_f.value or not modelo_f.value or not anio_f.value:
            snack(page, "Completa todos los campos", error=True)
            return
        try:
            anio = int(anio_f.value)
        except ValueError:
            snack(page, "El año debe ser un número", error=True)
            return
        res = api.crear_vehiculo(placa_f.value.upper(), marca_f.value,
                                  modelo_f.value, anio)
        if res["ok"]:
            vehiculo_actual_id[0] = res["data"]["id"]
            placa_f.value = marca_f.value = modelo_f.value = anio_f.value = ""
            snack(page, "Vehículo agregado ✓")
            cargar()
            if on_vehiculo_cambiado:
                on_vehiculo_cambiado(vehiculo_actual_id[0])
        else:
            snack(page, res.get("error", "Error"), error=True)

    cargar()

    return build_subpage(page, C, go_home, ft.Icons.TWO_WHEELER, "Mis vehículos", [
        section_title("MIS VEHÍCULOS", c),
        lista,
        section_title("AGREGAR VEHÍCULO", c),
        ft.Container(margin=ft.Margin(16, 0, 16, 10), content=placa_f),
        ft.Container(margin=ft.Margin(16, 0, 16, 10), content=marca_f),
        ft.Container(margin=ft.Margin(16, 0, 16, 10), content=modelo_f),
        ft.Container(margin=ft.Margin(16, 0, 16, 10), content=anio_f),
        ft.Container(
            margin=ft.Margin(16, 4, 16, 0),
            height=46, border_radius=10,
            bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
            on_click=agregar,
            content=ft.Text("Agregar vehículo", color="#FFFFFF", size=14,
                            weight=ft.FontWeight.BOLD),
        ),
    ])
