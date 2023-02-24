class DataEntry:

    def menu(self) -> str:
        languages = ['es_ES', 'en_US', 'eo_WORLD', 'de_DE', 'it_IT', 'la_VAT', 'ru_RU']
        language = int(input('Translator:\n\n 0) Spanish \n 1) English \n 2) Esperanto \n 3) German \n 4) Italian \n 5) Latin \n 6) Russian \n\n press the root language: '))
        return languages[language]

    def paragraphs(self) -> str:
        paragraph = input('enter the paragraph in the root language: ')
        return paragraph