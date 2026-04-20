import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()

    def llanta_section(titulo):
        return [
            section_title(titulo, c),
            text_field("Marca", "Ej: Pirelli, Michelin...", ft.Icons.LABEL, c),
            text_field("Referencia", "Ej: 110/70-17...", ft.Icons.NUMBERS, c),
            text_field("Presión recomendada (PSI)", "Ej: 32 PSI", ft.Icons.COMPRESS, c),
            text_field("Presión actual (PSI)", "Ej: 30 PSI", ft.Icons.COMPRESS, c),
            date_field("Último cambio", c),
            text_field("Porta sprocket (si aplica)", "Ej: 42 dientes", ft.Icons.SETTINGS, c),
        ]

    return build_subpage(page, C, go_home, ft.Icons.TIRE_REPAIR, "Llantas de aire", [
        *llanta_section("LLANTA DELANTERA"),
        *llanta_section("LLANTA TRASERA"),
        save_btn(c),
    ])
