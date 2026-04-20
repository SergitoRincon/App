import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.BOLT, "Bujías", [
        section_title("INFORMACIÓN", c),
        text_field("Marca", "Ej: NGK, Bosch, Denso...", ft.Icons.LABEL, c),
        text_field("Referencia", "Ej: CR7HSA, DR8EA...", ft.Icons.NUMBERS, c),
        section_title("CAMBIO / REVISIÓN", c),
        date_field("Último cambio", c),
        text_field("Kilometraje en el cambio", "Ej: 8450", ft.Icons.SPEED, c),
        text_field("Próximo cambio (km)", "Ej: 14450", ft.Icons.UPCOMING, c),
        save_btn(c),
    ])
