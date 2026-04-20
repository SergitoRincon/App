import flet as ft
from pages._mant_base import build_mant_page


def build(page, C, go_home, navigate_to, vehiculo_id_ref):
    c = C()
    return build_mant_page(
        page, C, go_home, navigate_to,
        ft.Icons.LIGHTBULB, "Bombillas secundarias", "bombillas_secundarias", vehiculo_id_ref,
        [
            ("LUZ TRASERA / STOP", [
                ("ref_stop", ft.TextField(label="Referencia", hint_text="Ej: BA15S P21W...",
                                prefix_icon=ft.Icons.NUMBERS,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("fecha_stop", ft.TextField(label="Último cambio", hint_text="DD/MM/AAAA",
                                prefix_icon=ft.Icons.CALENDAR_TODAY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
            ("DIRECCIONALES", [
                ("ref_dir", ft.TextField(label="Referencia", hint_text="Ej: BA15S P21W...",
                                prefix_icon=ft.Icons.NUMBERS,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("fecha_dir", ft.TextField(label="Último cambio", hint_text="DD/MM/AAAA",
                                prefix_icon=ft.Icons.CALENDAR_TODAY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
            ("TABLERO / INSTRUMENTOS", [
                ("ref_tab", ft.TextField(label="Referencia", hint_text="Ej: T10 W5W...",
                                prefix_icon=ft.Icons.NUMBERS,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
                ("fecha_tab", ft.TextField(label="Último cambio", hint_text="DD/MM/AAAA",
                                prefix_icon=ft.Icons.CALENDAR_TODAY,
                                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                                label_style=ft.TextStyle(color=c["GRAY"]),
                                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)),
            ]),
        ]
    )