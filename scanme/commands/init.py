import os
import sys
import yaml
import json
from .base import Base
from .utils import dir_metatree

"""The init command."""


class Init(Base):

    def run(self):

        level = 2

        if len(sys.argv) == 3:
            try:
                level = int(sys.argv[-1])
            except:
                pass

        data = dir_metatree()

        as_string = yaml.dump(json.loads(json.dumps(data)), allow_unicode=True)

        content = '# FORMAT\n```yaml\n{}```'.format(as_string)

        print(content)
