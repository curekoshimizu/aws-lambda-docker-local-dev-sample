import connexion  # type: ignore


def build_app() -> connexion.App:
    options = {"swagger_ui": True}
    app = connexion.App(__name__, specification_dir="openapi", options=options)
    app.add_api(
        "openapi.yaml",
        arguments={"title": "server"},
        validate_responses=True,
        pythonic_params=True,
    )

    return app
