import reflex as rx

# Comun


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'"),

preview = "/preview.png"

_meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@GhostH4ck"},
    ]

# Index

index_title = "GhostH4ck | Practicando programación web"
index_description = "Hola mi nombre es André Bayona, estoy creando mi web para practicar programación web y subir mis proyectos."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]

index_meta.extend(_meta)

# Proyects

proyects_title = "GhostH4ck | Proyectos de programación"
proyects_description = "Mi web donde publico mis proyectos de Programación web, C++, Python, Java..."

proyects_meta = [
    {"name": "og:title", "content": proyects_title},
    {"name": "og:description", "content": proyects_description},
]

proyects_meta.extend(_meta)


