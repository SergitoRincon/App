import flet as ft
from pages._mant_base import build_mant_page


def build(page, C, go_home, navigate_to, vehiculo_id_ref):
    c = C()
    return build_mant_page(
        page, C, go_home, navigate_to,
        ft.Icons.AIR, "Filtro de aire", "filtro_aire", vehiculo_id_ref,
        [
            ("INFORMACIÓN", [
                ("tipo", ft.TextField(label="Tipo", hint_text="Ej: Papel, Espuma, K&N...",
                                prefix_icon=ft.Icons.CATEGORY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("marca", ft.TextField(label="Marca", hint_text="Ej: K&N, Mann, Fram...",
                                prefix_icon=ft.Icons.LABEL,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
            ("MANTENIMIENTO", [
                ("fecha_cambio", ft.TextField(label="Último cambio", hint_text="DD/MM/AAAA",
                                prefix_icon=ft.Icons.CALENDAR_TODAY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("fecha_rev", ft.TextField(label="Última revisión", hint_text="DD/MM/AAAA",
                                prefix_icon=ft.Icons.CALENDAR_TODAY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("km_cambio", ft.TextField(label="Km en el cambio", hint_text="Ej: 8450",
                                prefix_icon=ft.Icons.SPEED,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("km_proximo", ft.TextField(label="Próximo cambio (km)", hint_text="Ej: 10450",
                                prefix_icon=ft.Icons.UPCOMING,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
        ]
    )