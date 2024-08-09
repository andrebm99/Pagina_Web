import reflex as rx
from ronaldev_bio.components.link_button import link_button
from ronaldev_bio.components.title import title
from ronaldev_bio.styles.styles import Size as Size
import ronaldev_bio.constants as const

def proyects_links() -> rx.Component:
    return rx.vstack(
        title("Proyectos"),
        
        link_button(
            "Java",
            "Repositorio de proyectos con Java",
            "/icons/java.svg",
            const.JAVA_URL
        ),

        link_button(
            "Python",
            "Repositorio de proyectos con Python",
            "/icons/python.svg",
            const.PYTHON_URL
        ),
        
        link_button(
            "JavaScript",
            "Repositorio de proyectos con JavaScript",
            "/icons/js.svg",
            const.GITHUB_URL
        ),
        
        link_button(
            "HTML - CSS",
            "Repositorio de proyectos Programación-Web",
            "/icons/html5.svg",
            const.PROGRAMACIONWEB_URL
        ),
        
        
        link_button(
            "Hack The Box",
            "Hacking y Ciberseguridad",
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