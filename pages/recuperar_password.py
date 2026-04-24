import flet as ft


def build(page: ft.Page, C, go_back):
    c = C()
    paso = [1]

    email_f = ft.TextField(
        label="Correo electrónico", hint_text="tu@email.com",
        prefix_icon=ft.Icons.EMAIL, keyboard_type=ft.KeyboardType.EMAIL,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)

    codigo_f = ft.TextField(
        label="Código de 6 dígitos", hint_text="123456",
        prefix_icon=ft.Icons.VERIFIED, keyboard_type=ft.KeyboardType.NUMBER,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
        visible=False)

    nueva_f = ft.TextField(
        label="Nueva contraseña", password=True, can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
        visible=False)

    confirmar_f = ft.TextField(
        label="Confirmar contraseña", password=True, can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_RESET,
        border_color=c["BORDER"], focused_border_color=c["ACCENT"],
        label_style=ft.TextStyle(color=c["GRAY"]),
        color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
        visible=False)

    error_t  = ft.Text("", color="#F44336", size=12, text_align=ft.TextAlign.CENTER)
    titulo_t = ft.Text("Recuperar contraseña", size=20, weight=ft.FontWeight.BOLD,
                        color=c["WHITE"], text_align=ft.TextAlign.CENTER)
    sub_t    = ft.Text("Ingresa tu correo para recibir un código",
                        size=13, color=c["GRAY"], text_align=ft.TextAlign.CENTER)
    btn_t    = ft.Text("Enviar código", color="#FFFFFF", size=15,
                        weight=ft.FontWeight.BOLD)

    def on_accion(e):
        import api_client as api
        error_t.value = ""

        if paso[0] == 1:
            em = email_f.value.strip()
            if not em:
                error_t.value = "Ingresa tu correo"
                page.update()
                return
            btn_t.value = "Enviando..."
            page.update()
            res = api.solicitar_reset(em)
            if res["ok"]:
                paso[0] = 2
                sub_t.value = f"Código enviado a {em}\nRevisa tu bandeja de entrada"
                codigo_f.visible = True
                nueva_f.visible = True
                confirmar_f.visible = True
                email_f.disabled = True
                btn_t.value = "Cambiar contraseña"
                page.update()
            else:
                error_t.value = res.get("error", "Error al enviar código")
                btn_t.value = "Enviar código"
                page.update()

        elif paso[0] == 2:
            codigo = codigo_f.value.strip()
            nueva = nueva_f.value.strip()
            confirmar = confirmar_f.value.strip()

            if not codigo or not nueva or not confirmar:
                error_t.value = "Completa todos los campos"
                page.update()
                return
            if len(nueva) < 6:
                error_t.value = "La contraseña debe tener al menos 6 caracteres"
                page.update()
                return
            if nueva != confirmar:
                error_t.value = "Las contraseñas no coinciden"
                page.update()
                return

            btn_t.value = "Verificando..."
            page.update()
            res = api.confirmar_reset(email_f.value.strip(), codigo, nueva)
            if res["ok"]:
                paso[0] = 3
                titulo_t.value = "¡Contraseña actualizada!"
                sub_t.value = "Ya puedes iniciar sesión con tu nueva contraseña"
                codigo_f.visible = False
                nueva_f.visible = False
                confirmar_f.visible = False
                email_f.visible = False
                btn_t.value = "Volver al login"
                page.update()
            else:
                error_t.value = res.get("error", "Código inválido o expirado")
                btn_t.value = "Cambiar contraseña"
                page.update()

        elif paso[0] == 3:
            go_back()

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
                content=ft.Icon(ft.Icons.LOCK_RESET, color="#FFFFFF", size=46),
            ),
            ft.Container(height=12),
            titulo_t,
            ft.Container(height=4),
            sub_t,
            ft.Container(height=20),
            ft.Container(
                margin=ft.Margin(24, 0, 24, 0),
                padding=ft.Padding(20, 20, 20, 20),
                border_radius=16, bgcolor=c["CARD"],
                border=ft.border.all(1, c["BORDER"]),
                content=ft.Column(spacing=12, controls=[
                    email_f, codigo_f, nueva_f, confirmar_f, error_t,
                    ft.Container(
                        height=48, border_radius=10, bgcolor=c["ACCENT"],
                        alignment=ft.Alignment(0, 0), on_click=on_accion,
                        content=btn_t,
                    ),
                    ft.Container(
                        alignment=ft.Alignment(0, 0),
                        on_click=lambda e: go_back(),
                        content=ft.Text("← Volver al login",
                                        color=c["GRAY"], size=13,
                                        text_align=ft.TextAlign.CENTER),
                    ),
                ]),
            ),
            ft.Container(height=30),
        ],
    )
