import reflex as rx
from ronaldev_bio.components.link_button import link_button
from ronaldev_bio.components.title import title
from ronaldev_bio.styles.styles import Size as Size
import ronaldev_bio.constants as const
from ronaldev_bio.routes import Route

def index_links() -> rx.Component:
    return rx.vstack(
        title("Links"),
        
        link_button(
            "LinkedIn", 
            "Mi perfil pre-profesional de LinkedIn",
            "/icons/linkedin.svg",
            const.LINKEDIN_URL
        ),

        link_button(
            "GitHub", 
            "Mi repositorio de GitHub",
            "/icons/github.svg",
            const.GITHUB_URL   
        ),
        
        link_button(
            "Proyectos", 
            "Proyectos de Ingeniería de Software - UTP",
            "/icons/code.svg",
            Route.PROYECTS.value,
            is_external=False
        ),

        link_button(
            "Playlist - Metal", 
            "Buena música para programar ✌️😎",
            "/icons/spotify.svg",
            const.METAL_URL
        ),

        title("Contacto"),

        link_button(
            "Email", 
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        
        width = "100%",
        spacing=Size.DEFAULT.value
    )