import flet as ft


def nivel_color(n):
    n = max(0, min(100, n))
    if n >= 50:
        t = (n - 50) / 50.0
        r = int(255 * (1 - t))
        g = int(180 + 55 * t)
        b = int(50 * (1 - t))
    else:
        t = n / 50.0
        r = 220
        g = int(60 + 160 * t)
        b = 0
    return f"#{r:02X}{g:02X}{b:02X}"


def build_subpage(page, C, go_home, icon_name, title, body_controls):
    c = C()

    def _back_hover(e):
        e.control.bgcolor = "#1E4A90D9" if e.data == "true" else ft.Colors.TRANSPARENT
        page.update()

    header = ft.Container(
        bgcolor=c["CARD"],
        border=ft.border.only(bottom=ft.BorderSide(1, c["BORDER"])),
        padding=ft.Padding(10, 12, 16, 12),
        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=40, height=40, border_radius=20,
                    bgcolor=ft.Colors.TRANSPARENT,
                    alignment=ft.Alignment(0, 0),
                    on_hover=_back_hover,
                    on_click=lambda e: go_home(),
                    content=ft.Icon(ft.Icons.ARROW_BACK_IOS_NEW,
                                    color=c["ACCENT"], size=20),
                ),
                ft.Container(width=8),
                ft.Icon(icon_name, color=c["ACCENT"], size=26),
                ft.Container(width=8),
                ft.Text(title, size=20, weight=ft.FontWeight.BOLD, color=c["WHITE"]),
            ],
        ),
    )
    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[header, ft.Container(height=16), *body_controls,
                  ft.Container(height=20)],
    )


def info_card(label, value, c):
    return ft.Container(
        margin=ft.Margin(16, 0, 16, 10),
        padding=ft.Padding(16, 14, 16, 14),
        border_radius=12,
        bgcolor=c["CARD"],
        border=ft.border.all(1, c["BORDER"]),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(label, color=c["GRAY"], size=13),
                ft.Text(value, color=c["WHITE"], size=13,
                        weight=ft.FontWeight.BOLD),
            ],
        ),
    )


def section_title(text, c):
    return ft.Container(
        margin=ft.Margin(16, 4, 16, 6),
        content=ft.Text(text, color=c["ACCENT"], size=12,
                        weight=ft.FontWeight.BOLD),
    )


def text_field(label, hint, icon, c):
    return ft.Container(
        margin=ft.Margin(16, 0, 16, 10),
        content=ft.TextField(
            label=label, hint_text=hint,
            prefix_icon=icon,
            border_color=c["BORDER"],
            focused_border_color=c["ACCENT"],
            label_style=ft.TextStyle(color=c["GRAY"]),
            color=c["WHITE"],
            bgcolor=c["CARD"],
            border_radius=10,
        ),
    )


def date_field(label, c):
    return text_field(label, "DD/MM/AAAA", ft.Icons.CALENDAR_TODAY, c)


def save_btn(c):
    return ft.Container(
        margin=ft.Margin(16, 8, 16, 0),
        height=44, border_radius=10,
        bgcolor=c["ACCENT"],
        alignment=ft.Alignment(0, 0),
        content=ft.Text("Guardar", color="#FFFFFF", size=14,
                        weight=ft.FontWeight.BOLD),
    )


def toggle_card(label, subtitle, value, c):
    return ft.Container(
        margin=ft.Margin(16, 0, 16, 10),
        padding=ft.Padding(16, 12, 16, 12),
        border_radius=12,
        bgcolor=c["CARD"],
        border=ft.border.all(1, c["BORDER"]),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(spacing=2, controls=[
                    ft.Text(label, color=c["WHITE"], size=14),
                    ft.Text(subtitle, color=c["GRAY"], size=11),
                ]),
                ft.Switch(value=value, active_color=c["ACCENT"]),
            ],
        ),
    )
