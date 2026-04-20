import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()

    def bombilla(titulo):
        return [
            section_title(titulo, c),
            text_field("Tipo / Referencia", "Ej: T10, BA15S...", ft.Icons.NUMBERS, c),
            text_field("Marca", "Ej: Philips, Osram...", ft.Icons.LABEL, c),
            date_field("Último cambio", c),
        ]

    return build_subpage(page, C, go_home, ft.Icons.LIGHTBULB, "Bombillas secundarias", [
        *bombilla("LUZ TRASERA / STOP"),
        *bombilla("DIRECCIONALES DELANTERAS"),
        *bombilla("DIRECCIONALES TRASERAS"),
        *bombilla("LUZ DE POSICIÓN"),
        *bombilla("TABLERO / INSTRUMENTOS"),
        save_btn(c),
    ])
