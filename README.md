# Introduction

To autogenerate SCANME.md, you can globally `pip install scanme`, and type `scanme`. Default limits scanning up to 2 levels depth. Type `scanme --all` to produce `SCANME.md` content from all subdirectories.

# Usage
Running command `scanme init` generates `SCANME.md` file with formats under the `FORMAT` heading, as so:

```yaml
- '*': ''
  README.md: {'*': ''}
  src:
    - '*': ''
      main.py: {'*': ''}
      main.js: {'*': ''}
      core:
        - '*': ''
          app.py: {'*': ''}
  docs:
    - '*': ''
      index.md: {'*': ''}
```

The values at each level provide ability to specify [metaformat](https://book.mindey.com/metaformat/0001-metaform-philosophy/0001-metaform-philosophy.html) for each file and directory in the project by providing URLs to schema specifications.
