import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Horrorscope!! Boo :)")
        self._arguments()
        self.args_value = self.parser.parse_args()

        self._remove_error()

        self._check_valid_sign()

    def _arguments(self):
        self.parser.add_argument('--sign', '-s', help="Your Starsign")

    def _check_valid_sign(self):
        valid_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
                       'scorpio', 'sagittarirus', 'capricon',
                       'aquarius', 'pisces']
        if self.star_sign not in valid_signs:
            print(f"Star sign `{self.star_sign}` not recognised!")
            self.parser.print_help()
            exit(1)

    def get_star_sign(self):
        return self.star_sign

    def _remove_error(self):
        try:
            self.star_sign = self.args_value.sign.lower()
        except AttributeError:
            print("Enter your sign bruh -_-")
            self.parser.print_help()
            exit(1)
