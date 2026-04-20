import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()
    return build_subpage(page, C, go_home, ft.Icons.BATTERY_CHARGING_FULL, "Batería", [
        section_title("INFORMACIÓN", c),
        text_field("Marca", "Ej: Yuasa, Motobatt, BS...", ft.Icons.LABEL, c),
        text_field("Referencia", "Ej: YTX7L-BS...", ft.Icons.NUMBERS, c),
        text_field("Voltaje", "Ej: 12V", ft.Icons.ELECTRIC_BOLT, c),
        text_field("Amperaje (Ah)", "Ej: 6Ah", ft.Icons.NUMBERS, c),
        section_title("CAMBIO / REVISIÓN", c),
        date_field("Último cambio", c),
        date_field("Última revisión", c),
        text_field("Próximo cambio estimado", "Ej: 2026", ft.Icons.UPCOMING, c),
        save_btn(c),
    ])
