import reflex as rx
from ronaldev_bio.components.link_button import link_button
from ronaldev_bio.components.title import title
from ronaldev_bio.styles.styles import Size as Size
import ronaldev_bio.constants as const

def proyects_links() -> rx.Component:
    return rx.vstack(
        title("Proyectos"),
        
        link_button(
            "JavaScript",
            "Programando en javaScript",
            "/icons/js.svg",
            const.GITHUB_URL
        ),
        link_button(
            "HTML - CSS",
            "Practicando Programación-Web",
            "/icons/html5.svg",
            const.GITHUB_URL
        ),
        link_button(
            "Python",
            "Proyectos Python",
            "/icons/python.svg",
            const.GITHUB_URL
        ),
        link_button(
            "Java",
            "Proyectos Java",
            "/icons/java.svg",
            const.GITHUB_URL
        ),
        link_button(
            "Hack The Box",
            "Mis maquinas resueltas en HTB.",
            "/icons/htb.svg",
            const.HACKTHEBOX_URL
        ),

        link_button(
            "Playlist - Metal", 
            "Buena música para programar ✌️😎",
            "/icons/spotify.svg",
            const.METAL_URL
        ),
        width = "100%",
        spacing=Size.DEFAULT.value
    )