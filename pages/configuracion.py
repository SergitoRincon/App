import flet as ft
from pages.utils import build_subpage, info_card, section_title


def build(page, C, go_home, navigate_to):
    c = C()

    def toggle_row(label, subtitle=None, value=False):
        return ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12,
            bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(spacing=2, controls=[
                        ft.Text(label, color=c["WHITE"], size=14),
                        ft.Text(subtitle, color=c["GRAY"], size=11) if subtitle else ft.Container(),
                    ]),
                    ft.Switch(value=value, active_color=c["ACCENT"]),
                ],
            ),
        )

    return build_subpage(page, C, go_home, ft.Icons.SETTINGS, "Configuración", [
        section_title("APARIENCIA", c),
        toggle_row("Modo oscuro automático", "Según el sistema", value=True),
        section_title("NOTIFICACIONES", c),
        toggle_row("Alertas de mantenimiento",     value=True),
        toggle_row("Recordatorios de combustible", value=True),
        toggle_row("Alertas de documentos",        value=False),
        section_title("PRIVACIDAD", c),
        toggle_row("Compartir ubicación", value=False),
        toggle_row("Estadísticas de uso", value=True),
        section_title("DATOS", c),
        info_card("Versión",               "1.0.0", c),
        info_card("Última sincronización", "Hoy",   c),
    ])
