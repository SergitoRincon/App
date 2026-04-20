import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.FILTER_ALT, "Filtro de aceite", [
        section_title("INFORMACIÓN DEL FILTRO", c),
        text_field("Marca", "Ej: Bosch, Mann, WIX...", ft.Icons.LABEL, c),
        text_field("Referencia", "Ej: W712/75...", ft.Icons.NUMBERS, c),
        section_title("CAMBIO", c),
        date_field("Fecha del último cambio", c),
        text_field("Kilometraje en el cambio", "Ej: 8450", ft.Icons.SPEED, c),
        text_field("Próximo cambio (km)", "Ej: 9450", ft.Icons.UPCOMING, c),
        save_btn(c),
    ])
