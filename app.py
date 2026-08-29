from cli.main import create_parser


def main():

    parser = create_parser()

    args = parser.parse_args()

    if args.command == "index":

        print(f"Indexing: {args.pdf_path}")

    elif args.command == "search":

        print(f"Searching: {args.query}")

    else:

        parser.print_help()


if __name__ == "__main__":

    main()