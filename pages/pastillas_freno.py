import flet as ft
from pages.utils import build_subpage, section_title, text_field, date_field, save_btn


def build(page, C, go_home, navigate_to):
    c = C()

    def pastilla(titulo):
        return [
            section_title(titulo, c),
            text_field("Marca", "Ej: Brembo, EBC, Ferodo...", ft.Icons.LABEL, c),
            text_field("Referencia", "Ej: FA135...", ft.Icons.NUMBERS, c),
            date_field("Último cambio", c),
            text_field("Kilometraje en el cambio", "Ej: 8450", ft.Icons.SPEED, c),
            text_field("Próximo cambio (km)", "Ej: 18450", ft.Icons.UPCOMING, c),
        ]

    return build_subpage(page, C, go_home, ft.Icons.DISC_FULL, "Pastillas de freno", [
        *pastilla("PASTILLA DELANTERA"),
        *pastilla("PASTILLA TRASERA"),
        save_btn(c),
    ])
