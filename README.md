# Saa
> _Making Time Speak!_ 🎙️
Translating time into human-friendly spoken expressions

![Saa OpenJourny](watch.png)

**Saa** allows you to effortlessly translate time into human-friendly spoken expressions. The word `saa` means `hour` in Swahili, and this package aims to humanify time expression across languages. It is build using pure Python standard libraries.

```python
from datetime import time
from saa import Clock

clock = Clock("en")
clock("11:15") # 'quarter past eleven'

ur = Clock("da")
t = time(hour=7, minute=30)
ur(t) # 'halvotte'

muda = Clock("sw")
muda("7:29") # 'saa moja na dakika ishirini na tisa asubuhi'
```

## Features

- Convert time into spoken expressions in various languages.
- Easy-to-use API with a simple and intuitive design.
- Pure Python implementation with no external dependencies.
- Extensible architecture for adding support for additional languages using the plugin design pattern.
- Compatible with Python 3.6 and higher.

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

<details>
  <summary>Using Saa with LangChain 🦜🔗</summary>

```python
from datetime import datetime
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain import SerpAPIWrapper
from saa import Clock

search = SerpAPIWrapper()
clock = Clock("en")

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
    ),
    Tool(
        name="Saa",
        func=lambda x:  f"It is {clock(datetime.now())}",
        description=("A Current Timer teller. Use this more s about what is current "
                     "time, like 'what time is it?' or 'what is the current clock?'"),
        return_direct=False,
    ),
]

agent = initialize_agent(
    tools,
    OpenAI(temperature=0),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

if __name__ == "__main__":

    user_input = input("Human: ") 
    print(agent.run(user_input))
  ```
Example: 
Prompt: `How many minutes are left before it is a quarter past twelve? Think step by step` 

![image](https://github.com/Proteusiq/saa/assets/14926709/5244c159-5fc3-4ac6-a9fa-829f9cf6ece6)

</details>

<details>
  <summary>Adding New Language 💾</summary>

Using `Kiswahili` as an example of how to add a new language
 1. Create a folder under `saa/luga` directory, using the ISO 639-1 language code, with dunder init python file.
 ```bash
 mkdir saa/luga/sw && touch saa/luga/sw/__init__.py
 ```

 2. Contents of  `__init__.py` must have the following pattern
 ```python
from dataclasses import dataclass
from saa.core.language import Luga


@dataclass(init=False, eq=False, repr=False, frozen=False)
class LanguageName(Luga):
    ...

class Language(LanguageName):
    pass
 ```

So for `Swahili` the skeleton of `saa/luga/sw/__init__.py` would be:

```python
...

@dataclass(init=False, eq=False, repr=False, frozen=False)
class Swahili(Luga):
    ...

class Language(Swahili):
    pass
...
```

Since we are implementing `Luga`, our tasks now are to implement both the properties (`time`, `number_connector`, `connect_format`) and static methods (`time_logic`, `post_logic`).

In Swahili `class`, time is expressed in terms of hour first and then minutes. time_indicator is a placeholder for whatever changing logic, e.g. minute or minutes. For Swahili the logic is what part of the day it is, morning, noon, evenning or night.

```python
time = {
    "past": "saa {hour} na dakika {minute} time_indicator",
    "to": "saa {hour} kasoro dakika {minute} time_indicator",
    0: "saa {hour} time_indicator",
    15: "saa {hour} na robo time_indicator",
    45: "saa {hour} kasorobo time_indicator",
    30: "saa {hour} na nusu time_indicator",
}
```

The numbers connector is Swahili is `na`, and the connection format is "{tens_digits @ index 0} {[number_connector] @ index 1} {ones_digits @ index 2}"

```python
number_connector = "na"
connect_format = "{0} {1} {2}"
```

Given the implementations of Numbers converter, will include 11-19 even though we could deduced them as 20-50s. The numbers are as following:
```python
numbers = {
    0: "sifuri",
    1: "moja",
    2: "mbili",
    3: "tatu",
    4: "nne",
    5: "tano",
    6: "sita",
    7: "saba",
    8: "nane",
    9: "tisa",
    10: "kumi",
    11: "kumi na moja",
    12: "kumi na mbili",
    13: "kumi na tatu",
    14: "kumi na nne",
    15: "kumi na tano",
    16: "kumi na sita",
    17: "kumi na saba",
    18: "kumi na nane",
    19: "kumi na tisa",
    20: "ishirini",
    30: "thelathini",
    40: "arobaini",
    50: "hamsini",
}
```

The major task is on time logic. In Swahili, 7 AM is the first hour in the morning (asubuhi), while 7 PM is the first hour in the evenning (jioni). 6 AM is the 12th hour in the morning ( asubuhi), while 6 PM is the 12th hour in the evenning(jioni).

```
"""
 0 - 11 asubuhi 
 12 - 15 mchana 
 16 - 19 jioni
 20 - 23 usiku 
"""

day_divisions = {
        0: "asubuhi",
        1: "asubuhi",
        2: "asubuhi",
        3: "asubuhi",
        4: "asubuhi",
        5: "asubuhi",
        6: "asubuhi",
        7: "asubuhi",
        8: "asubuhi",
        9: "asubuhi",
        10: "asubuhi",
        11: "asubuhi",
        12: "mchana",
        13: "mchana",
        14: "mchana",
        15: "mchana",
        16: "jioni",
        17: "jioni",
        18: "jioni",
        19: "jioni",
        20: "usiku",
        21: "usiku",
        22: "usiku",
        23: "usiku",
    }

    @staticmethod
    def post_logic(text: str) -> str:
        return text
```

Time to write tests ...

</details>


## Supported Languages
![IMG_1009](https://github.com/Proteusiq/saa/assets/14926709/8562ac6e-eef6-4912-bfe8-b74141010f23)

**Saa** currently supports the following languages:

- English (`en`)
- Danish (`da`)
- Swahile(`sw`)

Coming ...
- French (`fr`)
- Spanish (`es`)
- German (`de`)
- Italian (`it`)

## Extending Language Support

One of the key strengths of **Saa** is its extensible architecture, allowing you to easily add support for additional languages. To add a new language, follow these steps:

1. Create a new directory under the `saa/luga` directory, using the ISO 639-1 language code as the filename (e.g., `fr` for French) and create a Python `__init__.py`.
2. Implement the necessary functions in the new file to translate time into spoken expressions of the target language.
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
