import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.CABLE, "Guaya de clutch", [
        section_title("LUBRICACIÓN", c),
        date_field("Última lubricación", c),
        text_field("Producto usado", "Ej: WD-40, aceite 3en1...", ft.Icons.LABEL, c),
        text_field("Próxima lubricación (km)", "Ej: 9000", ft.Icons.UPCOMING, c),
        section_title("CAMBIO / REVISIÓN", c),
        date_field("Último cambio", c),
        text_field("Kilometraje en el cambio", "Ej: 8450", ft.Icons.SPEED, c),
        text_field("Próximo cambio (km)", "Ej: 18450", ft.Icons.UPCOMING, c),
        save_btn(c),
    ])
