import flet as ft
from pages._mant_base import build_mant_page


def build(page, C, go_home, navigate_to, vehiculo_id_ref):
    c = C()
    return build_mant_page(
        page, C, go_home, navigate_to,
        ft.Icons.WATER_DROP, "Líquido de frenos", "liquido_frenos", vehiculo_id_ref,
        [
            ("INFORMACIÓN", [
                ("tipo", ft.TextField(label="Tipo (DOT)", hint_text="Ej: DOT 4",
                                prefix_icon=ft.Icons.NUMBERS,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("marca", ft.TextField(label="Marca", hint_text="Ej: Brembo, Motul...",
                                prefix_icon=ft.Icons.LABEL,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
            ("CAMBIO / REVISIÓN", [
                ("fecha_cambio", ft.TextField(label="Último cambio", hint_text="DD/MM/AAAA",
                                prefix_icon=ft.Icons.CALENDAR_TODAY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("km_cambio", ft.TextField(label="Km en el cambio", hint_text="Ej: 8450",
                                prefix_icon=ft.Icons.SPEED,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("km_proximo", ft.TextField(label="Próximo cambio (km)", hint_text="Ej: 18450",
                                prefix_icon=ft.Icons.UPCOMING,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
        ]
    )