
LANGUAGE    = 'eng'
VERBOSE     = False

# {english term : {language code : translation}}
TRANSLATIONS = {}
SNAKE_CASES  = {}

from .utils import snake_case

# ====================================================================================================
# Add a translation for an english term
# ====================================================================================================

def add(english, fr = None, **translations):
    """ Add translations of an english term

    Arguments
    ---------
    - english (str) : the english terme to translate
    - fr (str = None) : translation into fr
    - translation (dict of language code -> translation) : translations into other languages
    """
    sc_english = snake_case(english)

    if english not in TRANSLATIONS:
        TRANSLATIONS[english] = {}
        SNAKE_CASES[sc_english] = {}
    
    trans = TRANSLATIONS[english]
    sc = SNAKE_CASES[sc_english]

    for language, translation in {'fr': fr, **translations}.items():
        if translation is None:
            continue

        trans[language] = translation
        sc[language] = snake_case(translation)

# ====================================================================================================
# Add translations into a language
# ====================================================================================================

def add_dictionary(language, dictionary):
    """ Add a language dictionnay

    Arguments
    ---------
    - language (str) : language code
    - dictionary (dict of english -> translation in langugae) : translation dictionaty
    """
    for english, translation in dictionary.items():
        add(english, **{language: translation})

# ====================================================================================================
# Add translations into a language
# ====================================================================================================

def tr(english, language=None):

    if language is None:
        language = LANGUAGE

    if language == 'eng':
        return english
    
    d = TRANSLATIONS.get(english, None)
    if d is None:
        if VERBOSE:
            print(f"Translation : no translation for '{english}'")
        return english
    
    translation = d.get(language, None)
    if translation is None:
        if VERBOSE:
            print(f"Translation : '{english}' is not translated into '{language}', only {list(d.keys())}")
        return english
    
    return translation
    
    

