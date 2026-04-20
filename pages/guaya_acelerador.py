import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn, toggle_card


def build(page, C, go_home, navigate_to):
    c = C()
    es_guaya = ft.Ref[bool]()
    es_guaya.current = True

    guaya_content = ft.Column(controls=[
        section_title("LUBRICACIÓN", c),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            content=ft.TextField(
                label="Última lubricación", hint_text="DD/MM/AAAA",
                prefix_icon=ft.Icons.CALENDAR_TODAY,
                border_color=c["BORDER"], focused_border_color=c["ACCENT"],
                label_style=ft.TextStyle(color=c["GRAY"]),
                color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
            ),
        ),
        text_field("Producto usado", "Ej: WD-40...", ft.Icons.LABEL, c),
        section_title("CAMBIO / REVISIÓN", c),
        date_field("Último cambio", c),
        text_field("Próximo cambio (km)", "Ej: 18450", ft.Icons.UPCOMING, c),
    ])

    electronico_content = ft.Container(
        margin=ft.Margin(16, 0, 16, 10),
        padding=ft.Padding(16, 14, 16, 14),
        border_radius=12,
        bgcolor=c["CARD"],
        border=ft.border.all(1, c["BORDER"]),
        content=ft.Column(spacing=8, controls=[
            ft.Icon(ft.Icons.ELECTRIC_BOLT, color=c["ACCENT"], size=32),
            ft.Text("Acelerador electrónico (Throttle by Wire)",
                    color=c["WHITE"], size=14, text_align=ft.TextAlign.CENTER),
            ft.Text("No requiere lubricación de guaya.\nRevisar sensor y conexiones eléctricament.",
                    color=c["GRAY"], size=12, text_align=ft.TextAlign.CENTER),
        ]),
        alignment=ft.Alignment(0, 0),
    )

    body_ref = ft.Ref[ft.Column]()

    def on_toggle(e):
        body_ref.current.controls = [
            section_title("TIPO DE ACELERADOR", c),
            toggle_card("Acelerador por guaya",
                        "Desactiva si es electrónico (TbW)", e.control.value, c),
            guaya_content if e.control.value else electronico_content,
            save_btn(c),
        ]
        page.update()

    switch = ft.Switch(value=True, active_color=c["ACCENT"], on_change=on_toggle)

    return build_subpage(page, C, go_home, ft.Icons.CABLE, "Guaya de acelerador", [
        ft.Column(
            ref=body_ref,
            controls=[
                section_title("TIPO DE ACELERADOR", c),
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
                                ft.Text("Acelerador por guaya", color=c["WHITE"], size=14),
                                ft.Text("Desactiva si es electrónico (TbW)",
                                        color=c["GRAY"], size=11),
                            ]),
                            switch,
                        ],
                    ),
                ),
                guaya_content,
                save_btn(c),
            ],
        ),
    ])
