import flet as ft


def build(page: ft.Page, C, on_login_success):
    c = C()

    modo = ["login"]   # lista para mutabilidad

    email_f    = ft.TextField(
        label="Correo electrónico", hint_text="tu@email.com",
        prefix_icon=ft.Icons.EMAIL, keyboard_type=ft.KeyboardType.EMAIL,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)

    nombre_f   = ft.TextField(
        label="Nombre completo", hint_text="Tu nombre",
        prefix_icon=ft.Icons.PERSON, visible=False,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)

    pass_f     = ft.TextField(
        label="Contraseña", password=True, can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)

    error_t    = ft.Text("", color="#F44336", size=12,
                          text_align=ft.TextAlign.CENTER)
    loading    = ft.ProgressRing(width=22, height=22, visible=False,
                                  color=c["ACCENT"])
    titulo_t   = ft.Text("Bienvenido", size=26, weight=ft.FontWeight.BOLD,
                          color=c["WHITE"], text_align=ft.TextAlign.CENTER)
    sub_t      = ft.Text("Inicia sesión para continuar", size=13,
                          color=c["GRAY"], text_align=ft.TextAlign.CENTER)
    btn_t      = ft.Text("Iniciar sesión", color="#FFFFFF", size=14,
                          weight=ft.FontWeight.BOLD)
    toggle_t   = ft.Text("¿No tienes cuenta? Regístrate",
                          color=c["ACCENT"], size=12,
                          text_align=ft.TextAlign.CENTER)

    def cambiar_modo(e):
        if modo[0] == "login":
            modo[0] = "registro"
            titulo_t.value  = "Crear cuenta"
            sub_t.value     = "Regístrate gratis"
            nombre_f.visible = True
            btn_t.value     = "Registrarse"
            toggle_t.value  = "¿Ya tienes cuenta? Inicia sesión"
        else:
            modo[0] = "login"
            titulo_t.value  = "Bienvenido"
            sub_t.value     = "Inicia sesión para continuar"
            nombre_f.visible = False
            btn_t.value     = "Iniciar sesión"
            toggle_t.value  = "¿No tienes cuenta? Regístrate"
        error_t.value = ""
        page.update()

    def on_submit(e):
        import api_client as api
        error_t.value = ""
        loading.visible = True
        page.update()

        em = email_f.value.strip()
        pw = pass_f.value

        if not em or not pw:
            error_t.value = "Completa todos los campos"
            loading.visible = False
            page.update()
            return

        if modo[0] == "login":
            res = api.login(em, pw)
        else:
            nm = nombre_f.value.strip()
            if not nm:
                error_t.value = "Ingresa tu nombre"
                loading.visible = False
                page.update()
                return
            res = api.registrar(nm, em, pw)

        loading.visible = False
        if res["ok"]:
            on_login_success()
        else:
            error_t.value = res.get("error", "Error desconocido")
            page.update()

    w = min((page.width or 390), 420)

    return ft.Column(
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(height=30),
            ft.Container(
                width=80, height=80, border_radius=40,
                bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
                content=ft.Icon(ft.Icons.TWO_WHEELER, color="#FFFFFF", size=44),
            ),
            ft.Container(height=14),
            titulo_t,
            ft.Container(height=4),
            sub_t,
            ft.Container(height=24),
            ft.Container(
                width=w - 32,
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
                        ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                               controls=[loading]),
                        ft.Container(
                            height=46, border_radius=10,
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
                    ],
                ),
            ),
            ft.Container(height=30),
        ],
    )
