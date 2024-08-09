import reflex as rx
import ronaldev_bio.styles.styles as styles
from ronaldev_bio.styles.styles import Size as Size
from ronaldev_bio.styles.colors import TextColor as TextColor
from ronaldev_bio.styles.colors import Color as Color
from ronaldev_bio.routes import Route

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box( 
                rx.text("Ghost", as_="span", color=Color.LOGO1.value),
                rx.text("H4ck", as_="span", color=Color.LOGO2.value),
                style = styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),

        position = "sticky",
        bg = Color.BACKGROUND.value,
        padding_x = Size.BIG.value,
        padding_y = Size.DEFAULT.value,
        z_index = "999",
        top="0"
)
        
