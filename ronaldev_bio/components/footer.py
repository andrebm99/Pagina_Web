import reflex as rx
import datetime
import ronaldev_bio.constants as const
from ronaldev_bio.styles.styles import Size as Size
from ronaldev_bio.styles.colors import TextColor as TextColor
from ronaldev_bio.styles.colors import Color as Color
from ronaldev_bio.styles.styles import Size, spacing

# Parte inferior de la Pagina Web

def footer() -> rx.Component :
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height = Size.LOGO.value,
            weight = Size.LOGO.value,
            alt="Logotipo de ",
        ),
        rx.link(
            f"© {datetime.date.today().year} GhostH4ck by ANDRE BAYONA v1.",
            href= const.GITHUB_URL,
            is_external=True,
            font_size = Size.MEDIUM.value,
            padding_top=Size.DEFAULT.value,
        ),
        
        rx.link(
            rx.hstack(
                # Icono de GitHub - Footer
                rx.image(
                    src="/icons/github.svg",
                    height = Size.LARGE.value,
                    weight = Size.LARGE.value,
                    alt="Logo GitHub",
                ),
                rx.text(
                    "PRACTICANDO DESARROLLO DE SOFTWARE 🧑🏽‍💻 LIMA - PERÚ ❤️🇵🇪",
                    font_size = Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                )
            ),

            # Configuración hstack

            href=const.REPO_URL,
            is_external=True,
        ),

        # Configuración del vstack 

        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=spacing.ZERO.value,
        color=TextColor.FOOTER.value

    )
        