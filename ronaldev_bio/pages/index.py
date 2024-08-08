import reflex as rx
import ronaldev_bio.utils as utils
import ronaldev_bio.styles.styles as styles
from ronaldev_bio.views.header import header
from ronaldev_bio.components.navbar import navbar
from ronaldev_bio.components.footer import footer
from ronaldev_bio.views.index_links import index_links
from ronaldev_bio.styles.styles import Size as Size, spacing


@rx.page(
        
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.index_meta
)

def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                footer(),
                spacing=spacing.VERY_BIG.value,
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = Size.BIG.value,
                padding = Size.BIG.value,
                
            ),
            width="100%",
        ),
        
    )
