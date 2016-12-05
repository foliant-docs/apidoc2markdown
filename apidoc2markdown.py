__version__ = "0.1.0"


import argparse, json, os.path, sys
import jinja2


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--input",
        default=".",
        help="path to the directory with api_data.json and api_project.json (default: .)",
        metavar="APIDOC_LOCATION"
    )

    parser.add_argument(
        "-o", "--output",
        default="apidoc.md",
        help="path to the output Markdown file (default: apidoc.md)",
        metavar="OUTPUT"
    )

    parser.add_argument(
        "-t", "--template",
        default=os.path.join(os.path.dirname(__file__), "apidoc.md.j2"),
        help="Jinja2 template used for conversion",
        metavar="TEMPLATE"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="apidoc2markdown " + __version__
    )

    args = parser.parse_args()

    print("Parsing Apidoc JSON... ", end="")

    try:
        apidoc_metadata = json.load(
            open(os.path.join(args.input, "api_project.json"), encoding="utf8")
        )

        apidoc_data = json.load(
            open(os.path.join(args.input, "api_data.json"), encoding="utf8")
        )

    except (FileNotFoundError, OSError):
        sys.exit("No Apidoc files found.")

    print("Done!")

    print("Parsing the template... ", end="")

    env = jinja2.Environment(extensions=["jinja2.ext.do"])
    template = env.from_string(open(args.template, encoding="utf8").read())

    print("Done!")

    print("Baking Markdown... ", end="")

    with open(args.output, "w", encoding="utf8") as output:
        output.write(
            template.render(
                apidoc_metadata=apidoc_metadata,
                apidoc_data=apidoc_data
            )
        )
    print("Done!")

    print("---")

    print("Result: ", args.output)
