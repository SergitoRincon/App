import flet as ft
from pages.utils import build_subpage, section_title, save_btn


def build(page, C, go_home, navigate_to):
    c = C()

    def cat_chip(label, selected=False):
        return ft.Container(
            padding=ft.Padding(12, 8, 12, 8),
            border_radius=20,
            bgcolor=c["ACCENT"] if selected else c["CARD"],
            border=ft.border.all(1, c["ACCENT"] if selected else c["BORDER"]),
            content=ft.Text(label,
                            color="#FFFFFF" if selected else c["GRAY"],
                            size=12),
        )

    def tarea_row(titulo, descripcion, nivel):
        colores = {"Alta": "#F44336", "Media": "#FFC107", "Baja": "#4CAF50"}
        return ft.Container(
            margin=ft.Margin(16, 0, 16, 10),
            padding=ft.Padding(16, 14, 16, 14),
            border_radius=12,
            bgcolor=c["CARD"],
            border=ft.border.all(1, c["BORDER"]),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(spacing=4, expand=True, controls=[
                        ft.Text(titulo, color=c["WHITE"], size=13,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(descripcion, color=c["GRAY"], size=11),
                    ]),
                    ft.Container(
                        padding=ft.Padding(8, 4, 8, 4),
                        border_radius=8,
                        bgcolor=colores.get(nivel, c["ACCENT"]),
                        content=ft.Text(nivel, size=11, color="#FFFFFF"),
                    ),
                ],
            ),
        )

    return build_subpage(page, C, go_home, ft.Icons.CATEGORY,
                         "Categorías de mantenimiento", [
        section_title("FILTRAR POR CATEGORÍA", c),
        ft.Container(
            margin=ft.Margin(16, 0, 16, 16),
            content=ft.Row(
                wrap=True, spacing=8, run_spacing=8,
                controls=[
                    cat_chip("Todos", selected=True),
                    cat_chip("Motor"),
                    cat_chip("Frenos"),
                    cat_chip("Kit de arrastre"),
                    cat_chip("Eléctrico"),
                    cat_chip("Llantas"),
                    cat_chip("Lubricación"),
                ],
            ),
        ),
        section_title("TAREAS PENDIENTES — ALTA PRIORIDAD", c),
        tarea_row("Licencia vencida", "Vencida desde Jun 2024", "Alta"),
        tarea_row("Cambio de aceite", "Próximo en 500 km", "Alta"),
        section_title("TAREAS PENDIENTES — MEDIA PRIORIDAD", c),
        tarea_row("Tensionar cadena", "Revisión en 200 km", "Media"),
        tarea_row("Revisar pastillas delantera", "Próxima revisión en 1,000 km", "Media"),
        section_title("TAREAS PENDIENTES — BAJA PRIORIDAD", c),
        tarea_row("Lubricar guaya de clutch", "Próxima lubricación en 2,000 km", "Baja"),
        tarea_row("Revisar presión de llantas", "Revisión mensual", "Baja"),
        save_btn(c),
    ])
