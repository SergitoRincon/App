import flet as ft


def build(page: ft.Page, C, on_login_success, on_recuperar=None):
    c = C()
    modo = ["login"]

    email_f  = ft.TextField(
        label="Correo electrónico", hint_text="tu@email.com",
        prefix_icon=ft.Icons.EMAIL, keyboard_type=ft.KeyboardType.EMAIL,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
        expand=True)

    nombre_f = ft.TextField(
        label="Nombre completo", hint_text="Tu nombre",
        prefix_icon=ft.Icons.PERSON, visible=False,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
        expand=True)

    pass_f   = ft.TextField(
        label="Contraseña", password=True, can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
        expand=True)

    error_t  = ft.Text("", color="#F44336", size=12,
                        text_align=ft.TextAlign.CENTER)
    titulo_t = ft.Text("Bienvenido", size=24, weight=ft.FontWeight.BOLD,
                        color=c["WHITE"], text_align=ft.TextAlign.CENTER)
    sub_t    = ft.Text("Inicia sesión para continuar", size=13,
                        color=c["GRAY"], text_align=ft.TextAlign.CENTER)
    btn_t    = ft.Text("Iniciar sesión", color="#FFFFFF", size=15,
                        weight=ft.FontWeight.BOLD)
    toggle_t = ft.Text("¿No tienes cuenta? Regístrate",
                        color=c["ACCENT"], size=13,
                        text_align=ft.TextAlign.CENTER)

    def cambiar_modo(e):
        if modo[0] == "login":
            modo[0]          = "registro"
            titulo_t.value   = "Crear cuenta"
            sub_t.value      = "Regístrate gratis"
            nombre_f.visible = True
            btn_t.value      = "Registrarse"
            toggle_t.value   = "¿Ya tienes cuenta? Inicia sesión"
        else:
            modo[0]          = "login"
            titulo_t.value   = "Bienvenido"
            sub_t.value      = "Inicia sesión para continuar"
            nombre_f.visible = False
            btn_t.value      = "Iniciar sesión"
            toggle_t.value   = "¿No tienes cuenta? Regístrate"
        error_t.value = ""
        page.update()

    def on_submit(e):
        import api_client as api
        em = email_f.value.strip()
        pw = pass_f.value.strip()
        error_t.value = ""
        if not em or not pw:
            error_t.value = "Completa todos los campos"
            page.update()
            return
        if modo[0] == "login":
            res = api.login(em, pw)
        else:
            nm = nombre_f.value.strip()
            if not nm:
                error_t.value = "Ingresa tu nombre"
                page.update()
                return
            res = api.registrar(nm, em, pw)
        if res["ok"]:
            on_login_success()
        else:
            error_t.value = res.get("error", "Error desconocido")
            page.update()

    return ft.Column(
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(height=20),
            ft.Container(
                width=84, height=84, border_radius=42,
                bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
                content=ft.Icon(ft.Icons.TWO_WHEELER,
                                color="#FFFFFF", size=46),
            ),
            ft.Container(height=12),
            titulo_t,
            ft.Container(height=4),
            sub_t,
            ft.Container(height=20),
            ft.Container(
                margin=ft.Margin(24, 0, 24, 0),
                padding=ft.Padding(20, 20, 20, 20),
                border_radius=16,
                bgcolor=c["CARD"],
                border=ft.border.all(1, c["BORDER"]),
                content=ft.Column(
                    spacing=12,
                    controls=[
                        nombre_f,
                        email_f,
                        pass_f,
                        error_t,
                        ft.Container(
                            height=48, border_radius=10,
                            bgcolor=c["ACCENT"],
                            alignment=ft.Alignment(0, 0),
                            on_click=on_submit,
                            content=btn_t,
                        ),
                        ft.Container(
                            alignment=ft.Alignment(0, 0),
                            on_click=cambiar_modo,
                            content=toggle_t,
                        ),
                        ft.Container(
                            alignment=ft.Alignment(0, 0),
                            on_click=lambda e: on_recuperar() if on_recuperar else None,
                            content=ft.Text(
                                "¿Olvidaste tu contraseña?",
                                color=c["GRAY"], size=12,
                                text_align=ft.TextAlign.CENTER),
                        ),
                    ],
                ),
            ),
            ft.Container(height=30),
        ],
    )
