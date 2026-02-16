INSTALLED_APPS = [
    # ...
    "rest_framework",
    "buscarPaises",   # tu app
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",  # útil en dev
    ]
}