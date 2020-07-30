import argparse
from argparse import Namespace


def read_cli_arguments() -> Namespace:
    parser = argparse.ArgumentParser(
        description="A mail sender")
    parser.add_argument(
        "--sender",
        required=True,
        help="Mail sender")

    parser.add_argument(
        "--recipients",
        nargs="+",
        required=True,
        help="Mail recipients")

    parser.add_argument(
        "--topic",
        required=True,
        help="Mail topic")

    parser.add_argument(
        "--body",
        required=True,
        help="Mail body")

    parser.add_argument(
        "--files",
        nargs="+",
        required=False,
        default=None,
        help="Files to send as attachment")

    parser.add_argument("--host", type=str,
                        help="server",
                        required=True)
    parser.add_argument("--port", type=str,
                        help="port",
                        required=True)
    parser.add_argument("--username", type=str,
                        help="Username",
                        required=False,
                        default="")
    parser.add_argument("--password", type=str,
                        help="Password",
                        required=False,
                        default="")

    return parser.parse_args()

