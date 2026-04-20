import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()

    def llanta_section(titulo, icono):
        return [
            section_title(titulo, c),
            text_field("Marca", "Ej: Pirelli, Michelin, Maxxis...", ft.Icons.LABEL, c),
            text_field("Referencia", "Ej: 110/70-17...", ft.Icons.NUMBERS, c),
            date_field("Último cambio", c),
            text_field("Kilometraje en el cambio", "Ej: 8450", ft.Icons.SPEED, c),
            text_field("Porta sprocket (si aplica)", "Ej: 42 dientes", ft.Icons.SETTINGS, c),
        ]

    return build_subpage(page, C, go_home, ft.Icons.TIRE_REPAIR, "Llantas", [
        *llanta_section("LLANTA DELANTERA", ft.Icons.TIRE_REPAIR),
        *llanta_section("LLANTA TRASERA", ft.Icons.TIRE_REPAIR),
        save_btn(c),
    ])
