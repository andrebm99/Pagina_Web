import reflex as rx
from ronaldev_bio.styles.styles import Size as Size
from ronaldev_bio.styles.colors import Color as Color, TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title, 
            as_ = "span",
            font_weight="bold", 
            color =Color.PRIMARY.value
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color = TextColor.BODY.value
    )