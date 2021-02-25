#!/usr/bin/env python3

from balancer.app import build_app


def main() -> None:
    application = build_app()
    application.run(port=9001)


if __name__ == "__main__":
    main()
