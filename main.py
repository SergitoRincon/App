import flet as ft
from pages import (
    perfil, mis_vehiculos, configuracion, cerrar_sesion,
    aceite, filtro_aire, filtro_aceite,
    cadena, pinon, sprocket,
    bujias, bateria, guaya_clutch, guaya_acelerador,
    llantas, llantas_aire, pastillas_freno,
    liquido_frenos, liquido_refrigerante, lineas_freno,
    bombilla_principal, bombillas_secundarias, bomba_aceite,
    categoria_mantenimiento,
    mapa, historial,
)
from pages.utils import nivel_color

USUARIO     = "Sergio"
PLACA       = "DUW79G"
MARCA       = "Benelli"
MODELO      = "180s"
ANIO        = "2022"
EXTRA_IMG   = None
PLACAS_MENU = ["DUW79G", "JHR45L"]

NAV_ITEMS = [
    ("imagenes/hogar.png",     "Inicio",    0),
    ("imagenes/mundo2.png",    "Mapa",      1),
    ("imagenes/historial.png", "Historial", 2),
]

# Secciones del grid con sus ítems
SECTIONS = [
    {
        "titulo": "Motor",
        "items": [
            ("imagenes/motocicleta.png", "Aceite",          "aceite"),
            (None,                       "Filtro de aire",  "filtro_aire"),
            (None,                       "Filtro de aceite","filtro_aceite"),
        ],
    },
    {
        "titulo": "Kit de arrastre",
        "items": [
            (None, "Cadena",   "cadena"),
            (None, "Piñón",    "pinon"),
            (None, "Sprocket", "sprocket"),
        ],
    },
    {
        "titulo": "Frenos y fluidos",
        "items": [
            (None, "Pastillas de freno",   "pastillas_freno"),
            (None, "Líquido de frenos",    "liquido_frenos"),
            (None, "Líq. refrigerante",    "liquido_refrigerante"),
        ],
    },
    {
        "titulo": "Eléctrico",
        "items": [
            (None, "Bujías",              "bujias"),
            (None, "Batería",             "bateria"),
            (None, "Bombilla principal",  "bombilla_principal"),
        ],
    },
    {
        "titulo": "Transmisión y cables",
        "items": [
            (None, "Guaya clutch",      "guaya_clutch"),
            (None, "Guaya acelerador",  "guaya_acelerador"),
            (None, "Líneas freno",      "lineas_freno"),
        ],
    },
    {
        "titulo": "Llantas y otros",
        "items": [
            (None, "Llantas",              "llantas"),
            (None, "Llantas de aire",      "llantas_aire"),
            (None, "Bombillas sec.",       "bombillas_secundarias"),
        ],
    },
    {
        "titulo": "General",
        "items": [
            (None, "Bomba de aceite",      "bomba_aceite"),
            (None, "Cat. mantenimiento",   "categoria_mantenimiento"),
            (None, "",                     None),   # espacio vacío
        ],
    },
]

LIGHT = {
    "BG": "#FFFFFF", "CARD": "#F2F2F7", "ACCENT": "#4A90D9",
    "WHITE": "#111111", "GRAY": "#666666", "BORDER": "#DDDDDD",
    "BAR": "#E0E0E0", "BOTTOM": "#F8F8F8",
}
DARK = {
    "BG": "#1C1C1E", "CARD": "#2C2C2E", "ACCENT": "#4A90D9",
    "WHITE": "#FFFFFF", "GRAY": "#AAAAAA", "BORDER": "#3A3A3C",
    "BAR": "#333333", "BOTTOM": "#1C1C1E",
}


def main(page: ft.Page):
    page.title         = "MotoApp"
    page.window.width  = 390
    page.window.height = 844
    page.padding       = ft.padding.only(bottom=70)

    def C():
        return DARK if page.platform_brightness == ft.Brightness.DARK else LIGHT

    def apply_theme():
        page.bgcolor = C()["BG"]
        page.theme_mode = (ft.ThemeMode.DARK
                           if page.platform_brightness == ft.Brightness.DARK
                           else ft.ThemeMode.LIGHT)
        page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE, use_material3=False)

    apply_theme()
    BTN_W = 105

    # ── Mapa de módulos ──────────────────────────────────
    PAGE_MAP = {
        "aceite":                 lambda: aceite.build(page, C, go_home, navigate_to),
        "filtro_aire":            lambda: filtro_aire.build(page, C, go_home, navigate_to),
        "filtro_aceite":          lambda: filtro_aceite.build(page, C, go_home, navigate_to),
        "cadena":                 lambda: cadena.build(page, C, go_home, navigate_to),
        "pinon":                  lambda: pinon.build(page, C, go_home, navigate_to),
        "sprocket":               lambda: sprocket.build(page, C, go_home, navigate_to),
        "bujias":                 lambda: bujias.build(page, C, go_home, navigate_to),
        "bateria":                lambda: bateria.build(page, C, go_home, navigate_to),
        "guaya_clutch":           lambda: guaya_clutch.build(page, C, go_home, navigate_to),
        "guaya_acelerador":       lambda: guaya_acelerador.build(page, C, go_home, navigate_to),
        "llantas":                lambda: llantas.build(page, C, go_home, navigate_to),
        "llantas_aire":           lambda: llantas_aire.build(page, C, go_home, navigate_to),
        "pastillas_freno":        lambda: pastillas_freno.build(page, C, go_home, navigate_to),
        "liquido_frenos":         lambda: liquido_frenos.build(page, C, go_home, navigate_to),
        "liquido_refrigerante":   lambda: liquido_refrigerante.build(page, C, go_home, navigate_to),
        "lineas_freno":           lambda: lineas_freno.build(page, C, go_home, navigate_to),
        "bombilla_principal":     lambda: bombilla_principal.build(page, C, go_home, navigate_to),
        "bombillas_secundarias":  lambda: bombillas_secundarias.build(page, C, go_home, navigate_to),
        "bomba_aceite":           lambda: bomba_aceite.build(page, C, go_home, navigate_to),
        "categoria_mantenimiento":lambda: categoria_mantenimiento.build(page, C, go_home, navigate_to),
    }
    MENU_MAP = {
        "Mi perfil":     lambda: perfil.build(page, C, go_home, navigate_to,
                                              USUARIO, PLACA, MARCA, MODELO, ANIO),
        "Mis vehiculos": lambda: mis_vehiculos.build(page, C, go_home, navigate_to, PLACAS_MENU),
        "Configuracion": lambda: configuracion.build(page, C, go_home, navigate_to),
        "Cerrar sesion": lambda: cerrar_sesion.build(page, C, go_home, navigate_to),
    }

    # ── Navegación ────────────────────────────────────────
    def go_home():
        top_overlay.visible     = False
        vehicle_overlay.visible = False
        content.content = build_home()
        _set_nav_active(0)
        page.update()

    def navigate_to(builder):
        top_overlay.visible     = False
        vehicle_overlay.visible = False
        content.content = builder()
        page.update()

    # ── Grid button ───────────────────────────────────────
    def grid_btn(img_path, label, key):
        c = C()
        if not key:   # celda vacía
            return ft.Container(width=BTN_W, height=80)

        icon_widget = (
            ft.Image(src=img_path, width=40, height=40, fit="contain")
            if img_path else
            ft.Container(
                width=34, height=34,
                bgcolor="#1E4A90D9",
                border_radius=10,
                alignment=ft.Alignment(0, 0),
                content=ft.Icon(ft.Icons.BUILD_CIRCLE, color=c["ACCENT"], size=20),
            )
        )

        def _hover(e):
            e.control.bgcolor = "#1E4A90D9" if e.data == "true" else ft.Colors.TRANSPARENT
            page.update()

        return ft.Container(
            width=BTN_W, height=80,
            border_radius=14,
            bgcolor=ft.Colors.TRANSPARENT,
            on_hover=_hover,
            on_click=lambda e, k=key: navigate_to(PAGE_MAP[k]) if k in PAGE_MAP else None,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=6,
                controls=[
                    icon_widget,
                    ft.Text(label, size=9, color=c["GRAY"],
                            text_align=ft.TextAlign.CENTER,
                            width=BTN_W - 6),
                ],
            ),
        )

    # ── Pantalla de inicio ────────────────────────────────
    def build_home():
        c = C()
        top = ft.Container(
            padding=ft.padding.only(left=20, right=10, top=16, bottom=10),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                width=46, height=46, border_radius=23,
                                bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
                                content=ft.Icon("person", color="#FFFFFF", size=24),
                            ),
                            ft.Text(f"Hola, {USUARIO}!", size=20,
                                    weight=ft.FontWeight.BOLD, color=c["WHITE"]),
                        ],
                    ),
                    ft.Container(
                        width=44, height=44, border_radius=22,
                        bgcolor=ft.Colors.TRANSPARENT,
                        alignment=ft.Alignment(0, 0),
                        on_click=toggle_top_menu,
                        on_hover=lambda e: (
                            setattr(e.control, "bgcolor",
                                    "#1E4A90D9" if e.data == "true" else ft.Colors.TRANSPARENT),
                            page.update(),
                        ),
                        content=ft.Icon(ft.Icons.MORE_VERT, color=c["WHITE"], size=28),
                    ),
                ],
            ),
        )

        card = ft.Container(
            margin=ft.margin.symmetric(horizontal=16),
            padding=ft.padding.symmetric(horizontal=20, vertical=14),
            border_radius=16, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
                controls=[
                    ft.Text(f"Tu vehículo: {PLACA}", size=12, color=c["GRAY"],
                            text_align=ft.TextAlign.CENTER),
                    ft.Text(f"{MARCA} {MODELO}, {ANIO}", size=20,
                            weight=ft.FontWeight.BOLD, color=c["WHITE"],
                            text_align=ft.TextAlign.CENTER),
                    ft.Container(width=48, height=3, border_radius=2, bgcolor=c["ACCENT"]),
                ],
            ),
        )

        # Secciones del grid
        section_controls = []
        for sec in SECTIONS:
            # Título de sección
            section_controls.append(
                ft.Container(
                    margin=ft.Margin(16, 12, 16, 4),
                    content=ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(width=3, height=16, border_radius=2,
                                         bgcolor=c["ACCENT"]),
                            ft.Container(width=8),
                            ft.Text(sec["titulo"], size=13,
                                    weight=ft.FontWeight.BOLD, color=c["WHITE"]),
                        ],
                    ),
                )
            )
            # Fila de botones
            items = sec["items"]
            section_controls.append(
                ft.Container(
                    margin=ft.Margin(16, 0, 16, 0),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[grid_btn(img, lb, key) for img, lb, key in items],
                    ),
                )
            )

        return ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                top,
                ft.Container(height=6),
                card,
                ft.Container(height=4),
                *section_controls,
                ft.Container(height=20),
            ],
        )

    # ── Overlays menú ─────────────────────────────────────
    def close_menu(e):
        vehicle_overlay.visible = False
        page.update()

    def close_top_menu(e):
        top_overlay.visible = False
        page.update()

    def build_menu_container():
        c = C()
        bg   = "#2C2C2C" if page.platform_brightness == ft.Brightness.DARK else "#FFFFFF"
        dark = page.platform_brightness == ft.Brightness.DARK
        return ft.Container(
            right=5, bottom=5, width=170, bgcolor=bg, border_radius=10,
            border=None if dark else ft.border.all(1, "#CCCCCC"),
            shadow=None if dark else ft.BoxShadow(blur_radius=12,
                color="#22000000", offset=ft.Offset(0, 4)),
            padding=ft.Padding(0, 8, 0, 8),
            content=ft.Column(tight=True, spacing=0, controls=[
                ft.TextButton(
                    width=170,
                    on_click=lambda e, p=placa: close_menu(e),
                    style=ft.ButtonStyle(
                        color=c["WHITE"],
                        bgcolor={ft.ControlState.HOVERED: "#2E4A90D9",
                                 ft.ControlState.DEFAULT: bg},
                        padding=ft.Padding(16, 10, 16, 10),
                        shape=ft.RoundedRectangleBorder(radius=0),
                        overlay_color="#2E4A90D9",
                    ),
                    content=ft.Text(placa, color=c["WHITE"], size=14,
                                    text_align=ft.TextAlign.LEFT),
                )
                for placa in PLACAS_MENU
            ]),
        )

    def build_top_menu_container():
        c = C()
        bg   = "#2C2C2C" if page.platform_brightness == ft.Brightness.DARK else "#FFFFFF"
        dark = page.platform_brightness == ft.Brightness.DARK
        return ft.Container(
            right=10, top=60, width=170, bgcolor=bg, border_radius=10,
            border=None if dark else ft.border.all(1, "#CCCCCC"),
            shadow=None if dark else ft.BoxShadow(blur_radius=12,
                color="#22000000", offset=ft.Offset(0, 4)),
            padding=ft.Padding(0, 8, 0, 8),
            content=ft.Column(tight=True, spacing=0, controls=[
                ft.TextButton(
                    width=170,
                    on_click=lambda e, p=item: (
                        close_top_menu(e),
                        navigate_to(MENU_MAP[p]) if p in MENU_MAP else None,
                    ),
                    style=ft.ButtonStyle(
                        color=c["WHITE"],
                        bgcolor={ft.ControlState.HOVERED: "#2E4A90D9",
                                 ft.ControlState.DEFAULT: bg},
                        padding=ft.Padding(16, 10, 16, 10),
                        shape=ft.RoundedRectangleBorder(radius=0),
                        overlay_color="#2E4A90D9",
                    ),
                    content=ft.Text(item, color=c["WHITE"], size=14,
                                    text_align=ft.TextAlign.LEFT),
                )
                for item in ["Mi perfil", "Mis vehiculos", "Configuracion", "Cerrar sesion"]
            ]),
        )

    vehicle_overlay = ft.Stack(
        visible=False, width=390, height=844,
        controls=[
            ft.Container(width=390, height=844,
                         bgcolor=ft.Colors.TRANSPARENT, on_click=close_menu),
            build_menu_container(),
        ],
    )
    top_overlay = ft.Stack(
        visible=False, width=390, height=844,
        controls=[
            ft.Container(width=390, height=844,
                         bgcolor=ft.Colors.TRANSPARENT, on_click=close_top_menu),
            build_top_menu_container(),
        ],
    )

    def toggle_menu(e):
        if top_overlay.visible:
            top_overlay.visible = False
        vehicle_overlay.visible = not vehicle_overlay.visible
        page.update()

    def toggle_top_menu(e):
        if vehicle_overlay.visible:
            vehicle_overlay.visible = False
        top_overlay.visible = not top_overlay.visible
        page.update()

    content = ft.Container(expand=True, bgcolor=C()["BG"], content=build_home())
    page.add(content)

    page.overlay.append(vehicle_overlay)
    page.overlay.append(top_overlay)

    # ── Nav buttons ───────────────────────────────────────
    def _set_nav_active(idx):
        c = C()
        for i, btn in enumerate(nav_btns):
            active = i == idx
            btn.content.controls[1].color = c["ACCENT"] if active else c["GRAY"]
            btn.bgcolor = "#404A90D9" if active else ft.Colors.TRANSPARENT

    def nav_btn(img_path, label, idx):
        c = C()

        def _hover(e):
            if e.control.bgcolor != "#404A90D9":
                e.control.bgcolor = "#1E4A90D9" if e.data == "true" else ft.Colors.TRANSPARENT
                page.update()

        return ft.Container(
            width=80, height=58, border_radius=10,
            bgcolor="#404A90D9" if idx == 0 else ft.Colors.TRANSPARENT,
            on_hover=_hover,
            on_click=lambda e, i=idx: switch(i),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=4, tight=True,
                controls=[
                    ft.Image(src=img_path, width=28, height=28, fit="contain")
                    if img_path else
                    ft.Container(width=28, height=28, alignment=ft.Alignment(0, 0),
                                 content=ft.Text("+", color=c["GRAY"], size=14)),
                    ft.Text(label, size=10,
                            color=c["ACCENT"] if idx == 0 else c["GRAY"]),
                ],
            ),
        )

    nav_btns = [nav_btn(img, lb, idx) for img, lb, idx in NAV_ITEMS]

    extra_btn = ft.Container(
        width=50, height=50, border_radius=12,
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.Alignment(0, 0),
        on_click=toggle_menu,
        content=ft.Text("+", color=C()["GRAY"], size=22,
                        text_align=ft.TextAlign.CENTER),
    )

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=C()["BOTTOM"], height=70,
        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[*nav_btns, ft.Container(expand=True), extra_btn],
        ),
    )

    NAV_SCREENS = {
        0: build_home,
        1: lambda: mapa.build(page, C, go_home, navigate_to),
        2: lambda: historial.build(page, C, go_home, navigate_to),
    }
    current_idx = [0]

    def switch(idx):
        current_idx[0] = idx
        _set_nav_active(idx)
        content.content = NAV_SCREENS[idx]()
        page.update()

    def on_brightness_change(e):
        apply_theme()
        content.bgcolor = C()["BG"]
        page.bgcolor    = C()["BG"]
        page.bottom_appbar.bgcolor = C()["BOTTOM"]
        vehicle_overlay.controls[1] = build_menu_container()
        top_overlay.controls[1]     = build_top_menu_container()
        switch(current_idx[0])

    page.on_platform_brightness_change = on_brightness_change
    page.update()


ft.app(target=main, assets_dir=".")
