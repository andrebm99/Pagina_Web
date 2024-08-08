import reflex as rx
import ronaldev_bio.utils as utils
from ronaldev_bio.routes import Route
from ronaldev_bio.components.navbar import navbar
from ronaldev_bio.views.header import header
from ronaldev_bio.views.proyects_links import proyects_links
from ronaldev_bio.components.footer import footer
import ronaldev_bio.styles.styles as styles
from ronaldev_bio.styles.styles import Size as Size, spacing

@rx.page(
        route=Route.PROYECTS.value,
        title=utils.proyects_title,
        description=utils.proyects_description,
        image=utils.preview,
        meta=utils.proyects_meta,
)


def proyects() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                proyects_links(),
                footer(),
                spacing=spacing.VERY_BIG.value,
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            ),
            
        ),
        
    )

