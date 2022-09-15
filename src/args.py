import argparse
import json
import string


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Horrorscope!! Boo :)",epilog="Another Terminal App made by brist0l 8)")
        self._arguments()
        self.args_value = self.parser.parse_args()

        self._self_checks()

    def _self_checks(self):
        self._remove_error()
        self._check_valid_sign()
        if self.args_value.save:
            self._save_file()

    def _arguments(self):
        self.parser.add_argument('--sign', '-s',type=string,metavar="Your Starsign", help="Your Starsign")
        self.parser.add_argument('--save',action='store_true',help="Save Your Starsign")

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
    def _save_file(self):
        # check if file exists
        # json format
        # if not print msg that it is making a new one
        data = {"Starsign":"Virgo"}
        # .Hscope is for debugging purposes
        with open('.Hscope','w') as f: # change it to ~/.Hscope
            json.dump(data,f)
        
