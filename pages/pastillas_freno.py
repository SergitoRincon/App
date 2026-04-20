import flet as ft
from pages._mant_base import build_mant_page


def build(page, C, go_home, navigate_to, vehiculo_id_ref):
    c = C()
    return build_mant_page(
        page, C, go_home, navigate_to,
        ft.Icons.DISC_FULL, "Pastillas de freno", "pastillas_freno", vehiculo_id_ref,
        [
            ("PASTILLA DELANTERA", [
                ("marca_del", ft.TextField(label="Marca", hint_text="Ej: Brembo, EBC...",
                                prefix_icon=ft.Icons.LABEL,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("ref_del", ft.TextField(label="Referencia", hint_text="Ej: FA135...",
                                prefix_icon=ft.Icons.NUMBERS,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("fecha_del", ft.TextField(label="Último cambio", hint_text="DD/MM/AAAA",
                                prefix_icon=ft.Icons.CALENDAR_TODAY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("km_del", ft.TextField(label="Km en el cambio", hint_text="Ej: 8450",
                                prefix_icon=ft.Icons.SPEED,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
            ("PASTILLA TRASERA", [
                ("marca_tra", ft.TextField(label="Marca", hint_text="Ej: Brembo, EBC...",
                                prefix_icon=ft.Icons.LABEL,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("ref_tra", ft.TextField(label="Referencia", hint_text="Ej: FA135...",
                                prefix_icon=ft.Icons.NUMBERS,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("fecha_tra", ft.TextField(label="Último cambio", hint_text="DD/MM/AAAA",
                                prefix_icon=ft.Icons.CALENDAR_TODAY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("km_tra", ft.TextField(label="Km en el cambio", hint_text="Ej: 8450",
                                prefix_icon=ft.Icons.SPEED,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
        ]
    )