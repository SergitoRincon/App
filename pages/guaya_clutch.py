import flet as ft
from pages._mant_base import build_mant_page


def build(page, C, go_home, navigate_to, vehiculo_id_ref):
    c = C()
    return build_mant_page(
        page, C, go_home, navigate_to,
        ft.Icons.CABLE, "Guaya de clutch", "guaya_clutch", vehiculo_id_ref,
        [
            ("LUBRICACIÓN", [
                ("fecha_lub", ft.TextField(label="Última lubricación", hint_text="DD/MM/AAAA",
                                prefix_icon=ft.Icons.CALENDAR_TODAY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("producto_lub", ft.TextField(label="Producto usado", hint_text="Ej: WD-40, aceite 3en1...",
                                prefix_icon=ft.Icons.LABEL,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("km_proximo_lub", ft.TextField(label="Próxima lubricación (km)", hint_text="Ej: 9000",
                                prefix_icon=ft.Icons.UPCOMING,
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