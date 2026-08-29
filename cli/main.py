import argparse


def create_parser():

    parser = argparse.ArgumentParser(

        prog="semantic-search-engine",

        description="Production Semantic Search Engine"

    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # Index command

    index_parser = subparsers.add_parser(
        "index"
    )

    index_parser.add_argument(
        "pdf_path",
        help="Path to the PDF file"
    )

    # Search command

    search_parser = subparsers.add_parser(
        "search"
    )

    search_parser.add_argument(
        "query",
        help="Search query"
    )

    return parser