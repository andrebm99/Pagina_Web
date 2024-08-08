import reflex as rx
from ronaldev_bio.components.link_icon import link_icon
from ronaldev_bio.components.title import title
from ronaldev_bio.components.info_text import info_text
from ronaldev_bio.styles.styles import Size as Size, spacing
from ronaldev_bio.styles.colors import Color, TextColor
import ronaldev_bio.constants as const


def header(details=True) -> rx.Component:
    return rx.vstack(
            rx.hstack(
                rx.box(
                    rx.avatar(
                        fallback="AB",
                        size= "7",
                        src="/avatar.jpg",
                        radius="full",
                        padding="2px",
                        Color = TextColor.BODY.value,
                        bg=Color.CONTENT.value,
                        border=f"4px solid {Color.BORDER.value}"
                    ),
                    position="relative"
                ),
                
                rx.vstack(
                    rx.heading(
                        "André Bayona",
                        spacing=Size.BIG.value,
                        color = TextColor.BODY.value,
                    ),
                    rx.text(
                        "@andre_bayona_99",
                        margin_top=Size.ZERO.value,
                        color = TextColor.USER.value
                    ),
                    rx.hstack(
                        link_icon(
                            "/icons/instagram.svg",
                            const.INSTAGRAM_URL,
                            "Instagram"
                        ),
                        link_icon(
                            "/icons/twitter.svg",
                            const.TWITTER_X_URL,
                            "Twitter"
                        ),
                        link_icon(
                            "/icons/spotify.svg",
                            const.SPOTIFY_URL,
                            "Spotify"
                        ),
                        spacing=Size.LARGE.value,
                        padding_top=Size.SMALL.value
                    ),
                    spacing=spacing.ZERO.value,
                    align_items="start"
                ),
                align="end",
                spacing=Size.BIG.value,
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    rx.text(
                        "Programación web | Java - Python | Ciberseguridad"
                    ),
                    width = "100%",
                    color = "#ff85a1",
                    font_size = Size.MEDIUM.value,
                    spacing=spacing.VERY_BIG.value
                ),
                rx.text(
                    
                    f"""
                    Soy un estudiante de 4to ciclo en Ingeniería de Software, responsabe y con habilidades destacadas para trabajar en equipo. Tengo conocimientos en Python, Java, SQL, Progración web y estoy aprendiendo ciberseguridad en Cisco. Mi objetivo es crecer en el desarrollo de software y contribuir significativamente en los proyectos."
                    """,
                    font_size = Size.DEFAULT.value,
                    color = TextColor.BODY.value
                ),
                width ="100%",
                spacing=spacing.BIG.value
            ),
            
        ),
        width="100%",
        spacing=spacing.BIG.value,
        align_items="start",
    )