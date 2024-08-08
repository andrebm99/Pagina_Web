import reflex as rx
import ronaldev_bio.styles.styles as styles
from ronaldev_bio.styles.styles import Size as Size, spacing


def link_button(
        title: str,
        body: str, 
        image: str,
        url: str, 
        is_external=True,
        ) -> rx.Component :
    
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(
                        title, 
                        size = spacing.SMALL.value,
                        style=styles.button_title_style
                    ),
                    rx.text(
                        body, 
                        size= spacing.VERY_SMALL.value,
                        style=styles.button_body_style
                    ),
                    align_items = "start",
                    size= spacing.VERY_SMALL.value,
                    margin=Size.ZERO.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=is_external,
        width="100%",
        
    )
