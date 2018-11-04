"""
scanme

Usage:
  scanme init
  scanme init <level>
  scanme -h | --help
  scanme --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  scanme init

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/wefindx/scanme
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import scanme.commands
    options = docopt(__doc__, version=VERSION)

    for (k, v) in options.items():

        if hasattr(scanme.commands, k) and v:
            module = getattr(scanme.commands, k)
            scanme.commands = getmembers(module, isclass)
            command = [command[1] for command in scanme.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
