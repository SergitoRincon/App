import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    aplica = ft.Ref[ft.Column]()

    content_aplica = ft.Column(controls=[
        section_title("INFORMACIÓN", c),
        text_field("Marca", "Ej: Honda, Motul, Peak...", ft.Icons.LABEL, c),
        text_field("Referencia / Tipo", "Ej: OAT, HOAT, convencional...", ft.Icons.NUMBERS, c),
        section_title("CAMBIO / REVISIÓN", c),
        date_field("Último cambio", c),
        text_field("Kilometraje en el cambio", "Ej: 8450", ft.Icons.SPEED, c),
        text_field("Próximo cambio (km)", "Ej: 18450", ft.Icons.UPCOMING, c),
        save_btn(c),
    ])

    content_aire = ft.Container(
        margin=ft.Margin(16, 10, 16, 10),
        padding=ft.Padding(16, 20, 16, 20),
        border_radius=12,
        bgcolor=c["CARD"],
        border=ft.border.all(1, c["BORDER"]),
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Icon(ft.Icons.AIR, color=c["ACCENT"], size=40),
                ft.Text("Motor refrigerado por aire", color=c["WHITE"], size=14,
                        text_align=ft.TextAlign.CENTER),
                ft.Text("No aplica líquido refrigerante.\nEl motor se enfría por circulación de aire.",
                        color=c["GRAY"], size=12, text_align=ft.TextAlign.CENTER),
            ],
        ),
    )

    body_col = ft.Column(ref=aplica, controls=[content_aplica])

    def on_toggle(e):
        body_col.controls = [content_aplica if e.control.value else content_aire]
        page.update()

    return build_subpage(page, C, go_home, ft.Icons.THERMOSTAT, "Líquido refrigerante", [
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 12, 16, 12),
            border_radius=12,
            bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(spacing=2, controls=[
                        ft.Text("Motor refrigerado por líquido", color=c["WHITE"], size=14),
                        ft.Text("Desactiva si es refrigerado por aire", color=c["GRAY"], size=11),
                    ]),
                    ft.Switch(value=True, active_color=c["ACCENT"], on_change=on_toggle),
                ],
            ),
        ),
        body_col,
    ])
