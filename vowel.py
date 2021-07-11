import string
def make_ing_form(passed_string):
    passed_string = passed_string.lower()
    letter = list(string.ascii_lowercase)
    vowel = ['a','e','i','o','u']
    consonant = [c for c in letter if c not in vowel]
    exception = ['be', 'see', 'flee', 'knee', 'lie']
    
    if passed_string.endswith('ie'):
      passed_string = passed_string[:-2]
      return passed_string + 'ying'
    elif passed_string.endswith('e'):
      if passed_string in exception:
        return passed_string + 'ing'
      else:
        passed_string = passed_string[:-1]
        return passed_string + 'ing'

    

    elif passed_string[-1] in consonant and passed_string[-2] in vowel and passed_string[-3] in consonant:
        passed_string += passed_string[-1]
        return passed_string + 'ing'
    else:
        return passed_string + 'ing'

verb = ['lie', 'see', 'move', 'hug', 'study']
for item in verb:
    print(make_ing_form(item))