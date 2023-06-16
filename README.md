# Saa
Translating time into human-friendly spoken expressions

![Saa OpenJourny](watch.png)

**Saa** allows you to effortlessly translate time into human-friendly spoken expressions. The word `saa` means `hour` in Swahili, and this package aims to humanify time expression across languages. It is build using pure Python standard libraries. 

```python
from datetime import time
from saa import Clock

clock = Clock("en")
clock("11:15") # 'quarter past eleven'

klok = Clock("da")
t = time(hour=7, minute=30)
klok(t) # 'halvotte'
```

## Features

- Convert time into spoken expressions in various languages.
- Easy-to-use API with a simple and intuitive design.
- Pure Python implementation with no external dependencies.
- Extensible architecture for adding support for additional languages using the plugin design pattern.
- Compatible with Python 3.8 and higher.

## Installation

You can install **Saa** using pip:

```shell
pip install -U saa
```

## Quick Start

Here's a simple example to get you started:

```python
from saa import Clock

# Create a Clock instance with the desired language (e.g., "en" for English)
clock = Clock("en")

# Translate time into a human-friendly spoken expression
# supports also datetime and time. .e.g. time(hour=11, minute=45) 
spoken_time = clock("11:45") 

print(spoken_time)  
# Output: "quarter to twelve"
```

## Supported Languages

**Saa** currently supports the following languages:

- English (`en`)
- Danish (`da`)

Coming ...
- Swahile(`sw`)
- French (`fr`)
- Spanish (`es`)
- German (`de`)
- Italian (`it`)

## Extending Language Support

One of the key strengths of **Saa** is its extensible architecture, allowing you to easily add support for additional languages. To add a new language, follow these steps:

1. Create a new directory under the `saa/lagu` directory, using the ISO 639-1 language code as the filename (e.g., `fr` for French) and create a Python `__init__.py`.
2. Implement the necessary functions in the new file to translate time into spoken expressions in the target language.
3. Test the new language integration thoroughly to ensure accurate and reliable translations.
4. Consider submitting a pull request to contribute your new language support to the main **Saa** repository.

We welcome contributions from the community to expand language support and make **Saa** even more versatile!

## Contributing

If you'd like to contribute to **Saa**, please follow the guidelines outlined in the [CONTRIBUTING.md](https://github.com/your-username/saa/blob/main/CONTRIBUTING.md) file. We appreciate your help in making this package better.

## License

**Saa** is released under the [MIT License](https://github.com/your-username/saa/blob/main/LICENSE). Feel free to use, modify, and distribute this package as per the terms of the license.

## Acknowledgments

I would like to express our future gratitude to the developers of French, Spanish, German, and Italian language plugins for their valuable contributions to the **Saa** package. 🤣

## Contact

For any questions, suggestions, or feedback, please reach out to our team at praysonpi<at>gmail.com.

Let **Saa** simplify time for you and enhance the way you communicate it across languages!
