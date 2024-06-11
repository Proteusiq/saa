class Converter:
    def __init__(self, language):
        self.language = language

    def __call__(self, number):
        return self.convert(number)

    def convert(self, number):
        if not -1 < number < 60:
            raise ValueError(f"{number} is outside the clock's range number `0-59`")
        readable_numbers = self.language.numbers
        translations_and = self.language.number_connector

        if number in readable_numbers:
            return readable_numbers[number]
        else:
            tens_digit = number - number % 10
            ones_digit = number % 10

            return self.language.connect_format.format(
                *[
                    readable_numbers[tens_digit],
                    translations_and,
                    readable_numbers[ones_digit],
                ]
            )
