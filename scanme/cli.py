"""
scanme

Usage:
  scanme dirs
  scanme dirs -a | --all
  scanme -h | --help
  scanme --version

Options:
  -a --all                          Does not ignore dot files
  -i --ignore                       Regex to igore
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  scanme

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
    # print(options)

    for (k, v) in options.items():

        if k in ['dirs']:
            k = 'init'

        if hasattr(scanme.commands, k) and v:
            module = getattr(scanme.commands, k)
            scanme.commands = getmembers(module, isclass)
            command = [command[1] for command in scanme.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
