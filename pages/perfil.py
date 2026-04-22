import threading
import flet as ft
from pages.utils import build_subpage, section_title, snack, show_loading, hide_loading
import api_client as api

SEP = "||"


def nombre_a_partes(nombre: str) -> tuple:
    if SEP in nombre:
        partes = nombre.split(SEP)
        while len(partes) < 4:
            partes.append("")
        return partes[0], partes[1], partes[2], partes[3]
    return nombre.strip(), "", "", ""


def partes_a_nombre(p1, p2, p3, p4) -> str:
    return SEP.join([p1, p2, p3, p4])


def nombre_visible(nombre: str) -> str:
    p1, p2, p3, p4 = nombre_a_partes(nombre)
    partes = [p for p in [p1, p2, p3, p4] if p.strip()]
    return " ".join(partes) if partes else nombre


def primer_nombre(nombre: str) -> str:
    p1, _, _, _ = nombre_a_partes(nombre)
    return p1 if p1 else (nombre.split()[0] if nombre else "")


def build(page, C, go_home, navigate_to, usuario_data: dict, foto_picker=None):
    c = C()

    nombre_raw = usuario_data.get("nombre", "")
    p1, p2, p3, p4 = nombre_a_partes(nombre_raw)
    email_val  = usuario_data.get("email", "")
    desde_val  = usuario_data.get("creado_en", "")[:10] if usuario_data.get("creado_en") else ""
    foto_val   = [usuario_data.get("foto") or ""]

    def mk_avatar():
        v = foto_val[0]
        if v and v.startswith("data:"):
            b64 = v.split(",", 1)[1] if "," in v else v
            return ft.Image(src_base64=b64, width=90, height=90,
                           border_radius=45, fit=ft.ImageFit.COVER)
        if v and v.startswith("http"):
            return ft.Image(src=v, width=90, height=90,
                           border_radius=45, fit=ft.ImageFit.COVER)
        return ft.Icon(ft.Icons.PERSON, color="#FFFFFF", size=48)

    avatar_box = ft.Container(
        width=90, height=90, border_radius=45,
        bgcolor=c["ACCENT"] if not foto_val[0] else ft.Colors.TRANSPARENT,
        alignment=ft.Alignment(0, 0),
        content=mk_avatar(),
    )

    nombre_display = ft.Text(
        nombre_visible(nombre_raw),
        size=18, weight=ft.FontWeight.BOLD, color=c["WHITE"])

    # ── Subir foto al backend ─────────────────────────
    def subir_foto(data_url: str):
        show_loading(page, "Subiendo foto...")
        res = api.actualizar_perfil({"foto": data_url})
        hide_loading(page)
        if res["ok"]:
            foto_val[0] = data_url
            usuario_data["foto"] = data_url
            avatar_box.bgcolor = ft.Colors.TRANSPARENT
            avatar_box.content = mk_avatar()
            page.update()
            snack(page, "Foto actualizada ✓")
        else:
            snack(page, res.get("error", "Error al subir foto"), error=True)

    def abrir_camara(e):
        _mostrar_dialogo_url()

    def _mostrar_dialogo_url():
        url_f = ft.TextField(
            label="URL de la imagen",
            hint_text="https://i.imgur.com/tu-foto.jpg",
            prefix_icon=ft.Icons.LINK,
            border_color=c["ACCENT"], focused_border_color=c["ACCENT"],
            label_style=ft.TextStyle(color=c["GRAY"]),
            color=c["WHITE"], bgcolor=c["CARD"], border_radius=10,
            value=foto_val[0] if foto_val[0] and foto_val[0].startswith("http") else "",
        )

        def cerrar(ev):
            dlg.open = False
            page.update()

        def confirmar(ev):
            dlg.open = False
            page.update()
            if url_f.value.strip():
                subir_foto(url_f.value.strip())

        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Foto de perfil", color=c["WHITE"],
                          weight=ft.FontWeight.BOLD),
            content=ft.Column(tight=True, spacing=10, controls=[
                ft.Text("Pega el enlace de tu foto",
                        color=c["GRAY"], size=13),
                url_f,
            ]),
            actions=[
                ft.TextButton("Cancelar",
                    style=ft.ButtonStyle(color=c["GRAY"]),
                    on_click=cerrar),
                ft.TextButton("Guardar",
                    style=ft.ButtonStyle(color=c["ACCENT"]),
                    on_click=confirmar),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            bgcolor=c["CARD"],
        )
        page.overlay.append(dlg)
        dlg.open = True
        page.update()

    # ── Campos del formulario ─────────────────────────
    def mk_field(label, value="", optional=False):
        return ft.TextField(
            label=f"{label} {'(opcional)' if optional else ''}".strip(),
            value=value,
            border_color=c["BORDER"], focused_border_color=c["ACCENT"],
            label_style=ft.TextStyle(color=c["GRAY"]),
            color=c["WHITE"], bgcolor=c["CARD"], border_radius=10)

    pn_f = mk_field("Primer nombre",    p1)
    sn_f = mk_field("Segundo nombre",   p2, optional=True)
    pa_f = mk_field("Primer apellido",  p3)
    sa_f = mk_field("Segundo apellido", p4, optional=True)

    def mostrar_exito():
        sb = ft.SnackBar(
            content=ft.Text("Datos actualizados con exito!"),
            bgcolor="#4CAF50", open=True,
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
        threading.Timer(1.0, quitar).start()

    def guardar(e):
        pn = pn_f.value.strip()
        if not pn:
            snack(page, "El primer nombre es obligatorio", error=True)
            return
        nombre_completo = partes_a_nombre(
            pn, sn_f.value.strip(), pa_f.value.strip(), sa_f.value.strip())
        show_loading(page, "Guardando...")
        res = api.actualizar_perfil({"nombre": nombre_completo})
        hide_loading(page)
        if res["ok"]:
            usuario_data["nombre"] = nombre_completo
            nombre_display.value = nombre_visible(nombre_completo)
            page.update()
            mostrar_exito()
        else:
            snack(page, res.get("error", "Error al guardar"), error=True)

    return build_subpage(page, C, go_home, ft.Icons.PERSON, "Mi perfil", [
        ft.Container(
            alignment=ft.Alignment(0, 0),
            margin=ft.Margin(0, 10, 0, 20),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
                controls=[
                    ft.Stack(
                        width=90, height=90,
                        controls=[
                            avatar_box,
                            ft.Container(
                                width=28, height=28,
                                border_radius=14,
                                bgcolor=c["ACCENT"],
                                border=ft.border.all(2, c["BG"]),
                                alignment=ft.Alignment(0, 0),
                                right=0, bottom=0,
                                on_click=abrir_camara,
                                content=ft.Icon(ft.Icons.CAMERA_ALT,
                                                color="#FFFFFF", size=14),
                            ),
                        ],
                    ),
                    nombre_display,
                    ft.Text(email_val, size=12, color=c["GRAY"]),
                ],
            ),
        ),
        section_title("EDITAR PERFIL", c),
        ft.Container(margin=ft.Margin(16, 0, 16, 10), content=pn_f),
        ft.Container(margin=ft.Margin(16, 0, 16, 10), content=sn_f),
        ft.Container(margin=ft.Margin(16, 0, 16, 10), content=pa_f),
        ft.Container(margin=ft.Margin(16, 0, 16, 10), content=sa_f),
        section_title("CUENTA", c),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text("Correo", color=c["GRAY"], size=13),
                    ft.Text(email_val, color=c["WHITE"], size=13,
                            weight=ft.FontWeight.BOLD),
                ],
            ),
        ),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12, bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text("Miembro desde", color=c["GRAY"], size=13),
                    ft.Text(desde_val, color=c["WHITE"], size=13,
                            weight=ft.FontWeight.BOLD),
                ],
            ),
        ),
        ft.Container(
            margin=ft.Margin(16, 8, 16, 0),
            height=46, border_radius=10,
            bgcolor=c["ACCENT"], alignment=ft.Alignment(0, 0),
            on_click=guardar,
            content=ft.Text("Guardar cambios", color="#FFFFFF",
                            size=14, weight=ft.FontWeight.BOLD),
        ),
    ])