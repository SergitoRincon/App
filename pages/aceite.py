import flet as ft
from pages._mant_base import build_mant_page

def build(page, C, go_home, navigate_to, vehiculo_id_ref):
    c = C()
    return build_mant_page(
        page, C, go_home, navigate_to,
        ft.Icons.OIL_BARREL, "Aceite", "aceite", vehiculo_id_ref,
        [
            ("INFORMACIÓN DEL ACEITE", [
                ("marca",      ft.TextField(label="Marca", hint_text="Ej: Castrol, Mobil...",
                                prefix_icon=ft.Icons.LABEL,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("referencia", ft.TextField(label="Referencia", hint_text="Ej: 10W40, 20W50...",
                                prefix_icon=ft.Icons.NUMBERS,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
            ("CAMBIO DE ACEITE", [
                ("fecha_cambio",    ft.TextField(label="Fecha último cambio", hint_text="DD/MM/AAAA",
                                    prefix_icon=ft.Icons.CALENDAR_TODAY,
                                    border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                    label_style=ft.TextStyle(color=c["GRAY"]),
                                    color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("km_cambio",       ft.TextField(label="Km en el cambio", hint_text="Ej: 8450",
                                    prefix_icon=ft.Icons.SPEED,
                                    border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                    label_style=ft.TextStyle(color=c["GRAY"]),
                                    color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("km_proximo",      ft.TextField(label="Próximo cambio (km)", hint_text="Ej: 9450",
                                    prefix_icon=ft.Icons.UPCOMING,
                                    border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                    label_style=ft.TextStyle(color=c["GRAY"]),
                                    color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("nivel",           ft.TextField(label="Nivel actual (%)", hint_text="Ej: 80",
                                    prefix_icon=ft.Icons.WATER_DROP,
                                    border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                    label_style=ft.TextStyle(color=c["GRAY"]),
                                    color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
        ]
    )