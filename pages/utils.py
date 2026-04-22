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


def W(page):
    w = page.width or 390
    return w if w > 100 else 390


# ── Loading overlay global ────────────────────────────────────────
_loading_overlay = None

def init_loading(page: ft.Page):
    global _loading_overlay
    _loading_overlay = ft.Container(
        visible=False,
        expand=True,
        bgcolor="#80000000",
        alignment=ft.Alignment(0, 0),
        content=ft.Container(
            width=120, height=120,
            border_radius=16,
            bgcolor="#2C2C2C",
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=12,
                controls=[
                    ft.ProgressRing(width=40, height=40, color="#4A90D9"),
                    ft.Text("Cargando...", color="#FFFFFF", size=12),
                ],
            ),
        ),
    )
    page.overlay.append(_loading_overlay)
    return _loading_overlay

def show_loading(page, msg="Cargando..."):
    if _loading_overlay:
        _loading_overlay.content.content.controls[1].value = msg
        _loading_overlay.visible = True
        page.update()

def hide_loading(page):
    if _loading_overlay:
        _loading_overlay.visible = False
        page.update()


# ── Popup de confirmación ─────────────────────────────────────────
def confirm_dialog(page, titulo, mensaje, on_confirm, c,
                   btn_confirm="Confirmar", btn_cancel="Cancelar",
                   danger=False):

    def close_dlg(e=None):
        dlg.open = False
        page.update()

    def confirm_and_close(e=None):
        dlg.open = False
        page.update()
        on_confirm()

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text(titulo, color=c["WHITE"], size=18,
                      weight=ft.FontWeight.BOLD),
        content=ft.Text(mensaje, color=c["GRAY"], size=14),
        actions=[
            ft.TextButton(
                btn_cancel,
                style=ft.ButtonStyle(color=c["GRAY"]),
                on_click=close_dlg,
            ),
            ft.TextButton(
                btn_confirm,
                style=ft.ButtonStyle(
                    color="#F44336" if danger else c["ACCENT"]),
                on_click=confirm_and_close,
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor=c["CARD"],
    )
    page.overlay.append(dlg)
    dlg.open = True
    page.update()


# ── Snackbar ──────────────────────────────────────────────────────
def snack(page, msg, error=False):
    page.snack_bar = ft.SnackBar(
        content=ft.Text(msg, color="#FFFFFF"),
        bgcolor="#F44336" if error else "#4CAF50",
        duration=3000,
    )
    page.snack_bar.open = True
    page.update()


# ── Header de subpágina ───────────────────────────────────────────
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
                ft.Text(title, size=20, weight=ft.FontWeight.BOLD,
                        color=c["WHITE"]),
            ],
        ),
    )
    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[header, ft.Container(height=16),
                  *body_controls, ft.Container(height=20)],
    )


# ── Tarjeta de info ───────────────────────────────────────────────
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
                ft.Text(str(value), color=c["WHITE"], size=13,
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


def text_field(label, hint, icon, c, value=""):
    return ft.Container(
        margin=ft.Margin(16, 0, 16, 10),
        content=ft.TextField(
            label=label, hint_text=hint,
            prefix_icon=icon,
            value=value,
            border_color=c["BORDER"],
            focused_border_color=c["ACCENT"],
            label_style=ft.TextStyle(color=c["GRAY"]),
            color=c["WHITE"],
            bgcolor=c["CARD"],
            border_radius=10,
        ),
    )


def date_field(label, c, value=""):
    return text_field(label, "DD/MM/AAAA", ft.Icons.CALENDAR_TODAY, c, value)


def save_btn(c, on_click=None, label="Guardar"):
    return ft.Container(
        margin=ft.Margin(16, 8, 16, 0),
        height=46, border_radius=10,
        bgcolor=c["ACCENT"],
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Text(label, color="#FFFFFF", size=14,
                        weight=ft.FontWeight.BOLD),
    )


def mostrar_exito(page, msg="Guardado correctamente ✓"):
    """Muestra un SnackBar verde que desaparece en 1 segundo."""
    import threading
    sb = ft.SnackBar(
        content=ft.Row(controls=[
            ft.Icon(ft.Icons.CHECK_CIRCLE, color="#FFFFFF", size=18),
            ft.Container(width=8),
            ft.Text(msg, color="#FFFFFF", size=13),
        ]),
        bgcolor="#4CAF50",
        open=True,
    )
    page.overlay.append(sb)
    page.update()
    def quitar():
        try:
            sb.open = False
            page.overlay.remove(sb)
            page.update()
        except Exception:
            pass
    threading.Thread(target=lambda: (__import__('time').sleep(1), quitar())).start()