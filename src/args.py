import argparse
class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Horrorscope!! Boo :)",epilog="Another Terminal App made by brist0l 8)")
        self._arguments()
        self.args_value = self.parser.parse_args()

        if self.args_value.sign:
            self.star_sign = self.args_value.sign.lower()
        self._self_checks()

    def _self_checks(self):
        if self.args_value.sign:
            self._check_valid_sign()
        if self.args_value.save:
            self._save_file()
       
    def get_args(self):
        if self.args_value.desc:
            return True
        else:  
            return False

    def _arguments(self):
        self.parser.add_argument('--sign', '-s',type=str,nargs='?',metavar="Your Starsign", help="Your Starsign")
        self.parser.add_argument('--save',action='store_true',help="Save Your Starsign")
        self.parser.add_argument('--desc','-d',action='store_true',help="Get Description Of Your Starsign")
        # forecast for today

    def _check_valid_sign(self):
        valid_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
                       'scorpio', 'sagittarirus', 'capricon',
                       'aquarius', 'pisces']
        if self.star_sign not in valid_signs:
            print(f"Star sign `{self.star_sign}` not recognised!")
            self.parser.print_help()
            exit(1)

    def get_star_sign(self):
        if not self.args_value.sign:
            try:
                with open(".Hscope",'r') as f:
                    self.star_sign = f.read()
            except FileNotFoundError:
                self.parser.print_help()
                exit(1)

        return self.star_sign


    def _save_file(self):
        with open('.Hscope','w') as f: # change it to ~/.Hscope
            if self.args_value.sign:
                f.write(self.star_sign)
            else:
                print("Enter Your Starsign Bruh -_-")
                self.parser.print_help()
                exit(1)
        
