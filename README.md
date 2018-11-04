# Introduction

To autogenerate SCANME.md, you can globally `pip install scanme`, and type `scanme init`.

# Usage
Running command `scanme init > SCANME.md` to generate `SCANME.md` content.

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
