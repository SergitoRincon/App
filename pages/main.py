"""
MotoApp — main.py
Multi-usuario, datos desde API, responsive, sin datos hardcodeados.
"""
import flet as ft
import api_client as api
from pages import (
    login as login_page,
    perfil, mis_vehiculos, configuracion, cerrar_sesion,
    aceite, filtro_aire, filtro_aceite,
    cadena, pinon, sprocket,
    bujias, bateria, guaya_clutch, guaya_acelerador,
    llantas, llantas_aire, pastillas_freno,
    liquido_frenos, liquido_refrigerante, lineas_freno,
    bombilla_principal, bombillas_secundarias, bomba_aceite,
    categoria_mantenimiento, mapa, historial,
)
from pages.utils import nivel_color

# Secciones del grid — sin datos hardcodeados
SECTIONS = [
    {"titulo": "Motor", "items": [
        ("imagenes/motocicleta.png", "Aceite",          "aceite"),
        (None,                       "Filtro de aire",  "filtro_aire"),
        (None,                       "Filtro de aceite","filtro_aceite"),
    ]},
    {"titulo": "Kit de arrastre", "items": [
        (None, "Cadena",   "cadena"),
        (None, "Piñón",    "pinon"),
        (None, "Sprocket", "sprocket"),
    ]},
    {"titulo": "Frenos y fluidos", "items": [
        (None, "Pastillas",        "pastillas_freno"),
        (None, "Líq. frenos",      "liquido_frenos"),
        (None, "Líq. refrigerante","liquido_refrigerante"),
    ]},
    {"titulo": "Eléctrico", "items": [
        (None, "Bujías",             "bujias"),
        (None, "Batería",            "bateria"),
        (None, "Bombilla principal", "bombilla_principal"),
    ]},
    {"titulo": "Transmisión y cables", "items": [
        (None, "Guaya clutch",     "guaya_clutch"),
        (None, "Guaya acelerador", "guaya_acelerador"),
        (None, "Líneas freno",     "lineas_freno"),
    ]},
    {"titulo": "Llantas y otros", "items": [
        (None, "Llantas",         "llantas"),
        (None, "Llantas de aire", "llantas_aire"),
        (None, "Bombillas sec.",  "bombillas_secundarias"),
    ]},
    {"titulo": "General", "items": [
        (None, "Bomba de aceite",   "bomba_aceite"),
        (None, "Cat. mantenimiento","categoria_mantenimiento"),
        (None, "",                   None),
    ]},
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
    page.title  = "MotoApp"
    page.padding = ft.padding.only(bottom=70)

    def C():
        return DARK if page.platform_brightness == ft.Brightness.DARK else LIGHT

    def apply_theme():
        page.bgcolor = C()["BG"]
        page.theme_mode = (ft.ThemeMode.DARK
                           if page.platform_brightness == ft.Brightness.DARK
                           else ft.ThemeMode.LIGHT)
        page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE, use_material3=False)

    apply_theme()

    # ── Estado de sesión ─────────────────────────────
    usuario_data   = [{}]       # datos del usuario actual
    vehiculo_id    = [None]     # id del vehículo activo
    vehiculo_info  = [{}]       # placa, marca, modelo, anio

    def W():
        return page.width or 390

    def BTN_W():
        # 3 botones en fila con margen lateral
        return max(90, int((W() - 48) / 3))

    # ── Páginas del menú superior ────────────────────
    def mk_menu_pages():
        return {
            "Mi perfil":     lambda: perfil.build(
                                 page, C, go_home, navigate_to,
                                 usuario_data[0]),
            "Mis vehiculos": lambda: mis_vehiculos.build(
                                 page, C, go_home, navigate_to,
                                 vehiculo_id,
                                 on_vehiculo_cambiado=_on_vehiculo_cambiado),
            "Configuracion": lambda: configuracion.build(page, C, go_home, navigate_to),
            "Cerrar sesion": lambda: cerrar_sesion.build(
                                 page, C, go_home, navigate_to,
                                 on_logout=show_login),
        }

    # ── Páginas de mantenimiento ─────────────────────
    def mk_grid_pages():
        vref = vehiculo_id
        return {
            "aceite":                  lambda: aceite.build(page, C, go_home, navigate_to, vref),
            "filtro_aire":             lambda: filtro_aire.build(page, C, go_home, navigate_to, vref),
            "filtro_aceite":           lambda: filtro_aceite.build(page, C, go_home, navigate_to, vref),
            "cadena":                  lambda: cadena.build(page, C, go_home, navigate_to, vref),
            "pinon":                   lambda: pinon.build(page, C, go_home, navigate_to, vref),
            "sprocket":                lambda: sprocket.build(page, C, go_home, navigate_to, vref),
            "bujias":                  lambda: bujias.build(page, C, go_home, navigate_to, vref),
            "bateria":                 lambda: bateria.build(page, C, go_home, navigate_to, vref),
            "guaya_clutch":            lambda: guaya_clutch.build(page, C, go_home, navigate_to, vref),
            "guaya_acelerador":        lambda: guaya_acelerador.build(page, C, go_home, navigate_to, vref),
            "llantas":                 lambda: llantas.build(page, C, go_home, navigate_to, vref),
            "llantas_aire":            lambda: llantas_aire.build(page, C, go_home, navigate_to, vref),
            "pastillas_freno":         lambda: pastillas_freno.build(page, C, go_home, navigate_to, vref),
            "liquido_frenos":          lambda: liquido_frenos.build(page, C, go_home, navigate_to, vref),
            "liquido_refrigerante":    lambda: liquido_refrigerante.build(page, C, go_home, navigate_to, vref),
            "lineas_freno":            lambda: lineas_freno.build(page, C, go_home, navigate_to, vref),
            "bombilla_principal":      lambda: bombilla_principal.build(page, C, go_home, navigate_to, vref),
            "bombillas_secundarias":   lambda: bombillas_secundarias.build(page, C, go_home, navigate_to, vref),
            "bomba_aceite":            lambda: bomba_aceite.build(page, C, go_home, navigate_to, vref),
            "categoria_mantenimiento": lambda: categoria_mantenimiento.build(page, C, go_home, navigate_to, vref),
        }

    # ── Contenedor principal ─────────────────────────
    content = ft.Container(expand=True, bgcolor=C()["BG"])
    page.add(content)

    # ── Overlays de menú ─────────────────────────────
    def close_menu(e=None):
        vehicle_overlay.visible = False
        page.update()

    def close_top_menu(e=None):
        top_overlay.visible = False
        page.update()

    def build_vehicle_overlay():
        c = C()
        bg   = "#2C2C2C" if page.platform_brightness == ft.Brightness.DARK else "#FFFFFF"
        dark = page.platform_brightness == ft.Brightness.DARK
        veh  = api.get_vehiculos()
        placas = [v["placa"] for v in veh["data"]] if veh["ok"] else []
        if not placas:
            placas = ["Sin vehículos"]
        return ft.Container(
            right=5, bottom=5, width=180, bgcolor=bg, border_radius=10,
            border=None if dark else ft.border.all(1, "#CCCCCC"),
            shadow=None if dark else ft.BoxShadow(
                blur_radius=12, color="#22000000", offset=ft.Offset(0, 4)),
            padding=ft.Padding(0, 8, 0, 8),
            content=ft.Column(tight=True, spacing=0, controls=[
                ft.TextButton(width=180, on_click=lambda e, p=pl: close_menu(e),
                    style=ft.ButtonStyle(
                        color=c["WHITE"],
                        bgcolor={ft.ControlState.HOVERED: "#2E4A90D9",
                                 ft.ControlState.DEFAULT: bg},
                        padding=ft.Padding(16, 10, 16, 10),
                        shape=ft.RoundedRectangleBorder(radius=0),
                        overlay_color="#2E4A90D9",
                    ),
                    content=ft.Text(pl, color=c["WHITE"], size=14,
                                    text_align=ft.TextAlign.LEFT),
                )
                for pl in placas
            ]),
        )

    def build_top_overlay():
        c = C()
        bg   = "#2C2C2C" if page.platform_brightness == ft.Brightness.DARK else "#FFFFFF"
        dark = page.platform_brightness == ft.Brightness.DARK
        MENU_PAGES = mk_menu_pages()
        return ft.Container(
            right=10, top=60, width=180, bgcolor=bg, border_radius=10,
            border=None if dark else ft.border.all(1, "#CCCCCC"),
            shadow=None if dark else ft.BoxShadow(
                blur_radius=12, color="#22000000", offset=ft.Offset(0, 4)),
            padding=ft.Padding(0, 8, 0, 8),
            content=ft.Column(tight=True, spacing=0, controls=[
                ft.TextButton(width=180,
                    on_click=lambda e, it=item: (
                        close_top_menu(e),
                        navigate_to(MENU_PAGES[it]) if it in MENU_PAGES else None,
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

    vehicle_overlay = ft.Stack(visible=False, width=390, height=844, controls=[
        ft.Container(width=390, height=844, bgcolor=ft.Colors.TRANSPARENT,
                     on_click=close_menu),
        ft.Container(),
    ])
    top_overlay = ft.Stack(visible=False, width=390, height=844, controls=[
        ft.Container(width=390, height=844, bgcolor=ft.Colors.TRANSPARENT,
                     on_click=close_top_menu),
        ft.Container(),
    ])

    def _refresh_overlays():
        vehicle_overlay.controls[1] = build_vehicle_overlay()
        top_overlay.controls[1]     = build_top_overlay()
        vehicle_overlay.width  = W()
        vehicle_overlay.height = page.height or 844
        top_overlay.width  = W()
        top_overlay.height = page.height or 844

    page.overlay.append(vehicle_overlay)
    page.overlay.append(top_overlay)

    def toggle_menu(e):
        if top_overlay.visible:
            top_overlay.visible = False
        _refresh_overlays()
        vehicle_overlay.visible = not vehicle_overlay.visible
        page.update()

    def toggle_top_menu(e):
        if vehicle_overlay.visible:
            vehicle_overlay.visible = False
        _refresh_overlays()
        top_overlay.visible = not top_overlay.visible
        page.update()

    # ── Nav bar ──────────────────────────────────────
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
                    ft.Container(width=28, height=28, alignment=ft.Alignment(0,0),
                                 content=ft.Text("+", color=c["GRAY"], size=14)),
                    ft.Text(label, size=10,
                            color=c["ACCENT"] if idx == 0 else c["GRAY"]),
                ],
            ),
        )

    NAV_ITEMS = [
        ("imagenes/hogar.png",     "Inicio",    0),
        ("imagenes/mundo2.png",    "Mapa",      1),
        ("imagenes/historial.png", "Historial", 2),
    ]
    nav_btns = [nav_btn(img, lb, idx) for img, lb, idx in NAV_ITEMS]

    extra_btn = ft.Container(
        width=50, height=50, border_radius=12,
        bgcolor=ft.Colors.TRANSPARENT, alignment=ft.Alignment(0,0),
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

    # ── Grid button ──────────────────────────────────
    def grid_btn(img_path, label, key):
        c = C()
        bw = BTN_W()
        if not key:
            return ft.Container(width=bw, height=80)

        icon_widget = (
            ft.Image(src=img_path, width=40, height=40, fit="contain")
            if img_path else
            ft.Container(width=34, height=34, bgcolor="#1E4A90D9",
                         border_radius=10, alignment=ft.Alignment(0,0),
                         content=ft.Icon(ft.Icons.BUILD_CIRCLE,
                                         color=c["ACCENT"], size=20))
        )
        def _hover(e):
            e.control.bgcolor = "#1E4A90D9" if e.data == "true" else ft.Colors.TRANSPARENT
            page.update()

        GRID_PAGES = mk_grid_pages()
        return ft.Container(
            width=bw, height=80, border_radius=14,
            bgcolor=ft.Colors.TRANSPARENT, on_hover=_hover,
            on_click=lambda e, k=key: navigate_to(GRID_PAGES[k]) if k in GRID_PAGES else None,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER, spacing=6,
                controls=[
                    icon_widget,
                    ft.Text(label, size=9, color=c["GRAY"],
                            text_align=ft.TextAlign.CENTER, width=bw - 6),
                ],
            ),
        )

    # ── Build home ───────────────────────────────────
    def build_home():
        c = C()
        w = W()
        nombre = usuario_data[0].get("nombre", "")
        vinfo  = vehiculo_info[0]
        placa  = vinfo.get("placa",  "Sin vehículo")
        marca  = vinfo.get("marca",  "")
        modelo = vinfo.get("modelo", "")
        anio   = vinfo.get("anio",   "")

        card_text = (f"{marca} {modelo}, {anio}" if marca
                     else "Agrega tu vehículo →")

        top = ft.Container(
            padding=ft.Padding(20, 16, 10, 10),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER,
                           controls=[
                        ft.Container(
                            width=46, height=46, border_radius=23,
                            bgcolor=c["ACCENT"], alignment=ft.Alignment(0,0),
                            content=ft.Icon("person", color="#FFFFFF", size=24),
                        ),
                        ft.Text(f"Hola, {nombre}!" if nombre else "Bienvenido",
                                size=20, weight=ft.FontWeight.BOLD, color=c["WHITE"]),
                    ]),
                    ft.Container(
                        width=44, height=44, border_radius=22,
                        bgcolor=ft.Colors.TRANSPARENT, alignment=ft.Alignment(0,0),
                        on_click=toggle_top_menu,
                        on_hover=lambda e: (
                            setattr(e.control, "bgcolor",
                                    "#1E4A90D9" if e.data=="true" else ft.Colors.TRANSPARENT),
                            page.update()),
                        content=ft.Icon(ft.Icons.MORE_VERT, color=c["WHITE"], size=28),
                    ),
                ],
            ),
        )

        card = ft.Container(
            margin=ft.Margin(16,0,16,0),
            padding=ft.Padding(20,14,20,14),
            border_radius=16, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            on_click=lambda e: navigate_to(
                lambda: mis_vehiculos.build(page, C, go_home, navigate_to,
                                            vehiculo_id, _on_vehiculo_cambiado)),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4,
                controls=[
                    ft.Text(f"Vehículo activo: {placa}", size=12, color=c["GRAY"],
                            text_align=ft.TextAlign.CENTER),
                    ft.Text(card_text, size=20, weight=ft.FontWeight.BOLD,
                            color=c["WHITE"], text_align=ft.TextAlign.CENTER),
                    ft.Container(width=48, height=3, border_radius=2,
                                 bgcolor=c["ACCENT"]),
                ],
            ),
        )

        section_controls = []
        for sec in SECTIONS:
            section_controls.append(
                ft.Container(
                    margin=ft.Margin(16, 10, 16, 4),
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
            section_controls.append(
                ft.Container(
                    margin=ft.Margin(8, 0, 8, 0),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[grid_btn(img, lb, key)
                                  for img, lb, key in sec["items"]],
                    ),
                )
            )

        return ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[top, ft.Container(height=6), card, ft.Container(height=4),
                      *section_controls, ft.Container(height=20)],
        )

    # ── Navegación ───────────────────────────────────
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

    current_idx = [0]

    def switch(idx):
        current_idx[0] = idx
        _set_nav_active(idx)
        NAV_SCREENS = {
            0: build_home,
            1: lambda: mapa.build(page, C, go_home, navigate_to, vehiculo_id),
            2: lambda: historial.build(page, C, go_home, navigate_to, vehiculo_id),
        }
        content.content = NAV_SCREENS[idx]()
        page.update()

    def _on_vehiculo_cambiado(vid):
        vehiculo_id[0] = vid
        veh = api.get_vehiculos()
        if veh["ok"]:
            for v in veh["data"]:
                if v["id"] == vid:
                    vehiculo_info[0] = v
                    break

    # ── Login / Logout ───────────────────────────────
    def show_login():
        page.bottom_appbar.visible = False
        vehicle_overlay.visible    = False
        top_overlay.visible        = False
        content.bgcolor = C()["BG"]
        content.content = login_page.build(page, C, on_login_success)
        page.update()

    def on_login_success():
        # Cargar datos del usuario
        u = api.get_perfil()
        if u["ok"]:
            usuario_data[0] = u["data"]

        # Cargar primer vehículo
        veh = api.get_vehiculos()
        if veh["ok"] and veh["data"]:
            vehiculo_id[0]   = veh["data"][0]["id"]
            vehiculo_info[0] = veh["data"][0]

        page.bottom_appbar.visible = True
        content.bgcolor = C()["BG"]
        content.content = build_home()
        _set_nav_active(0)
        page.update()

    # ── Inicio de la app ─────────────────────────────
    if api.sesion_activa():
        on_login_success()
    else:
        page.bottom_appbar.visible = False
        content.content = login_page.build(page, C, on_login_success)

    def on_brightness_change(e):
        apply_theme()
        content.bgcolor = C()["BG"]
        page.bgcolor    = C()["BG"]
        page.bottom_appbar.bgcolor = C()["BOTTOM"]
        _refresh_overlays()
        switch(current_idx[0])

    page.on_platform_brightness_change = on_brightness_change
    page.on_resized = lambda e: (
        content.update(),
        page.update(),
    )
    page.update()


ft.app(target=main, assets_dir=".")
