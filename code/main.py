import jinja2
import json
import time

ENCODING_FORMAT = 'utf-8'

LANGUAGES_LOCATION = 'code/languages/'
TEMPLATES_LOCATION = 'code/templates/'

TEMPLATE_FILE_NAME = 'README.md.j2'

LANGUAGES = ['EN', 'FR']
DEFAULT_LANGUAGE = 'EN'

def load_translation(language: str):
    with open(f"{LANGUAGES_LOCATION}{language.upper()}.json", 'r', encoding=ENCODING_FORMAT) as file:
        return json.load(file)

def generate_language_navigation_buttons(current_language):
    buttons = ''
    for language in LANGUAGES:
        if language.lower() == current_language.lower():
            continue
        
        buttons += f'[![{language}](https://img.shields.io/badge/{language}-blue)](https://github.com/Ferfoui/Ferfoui/blob/main/README_{language}.md)  '
    
    return buttons

def render_readme_template(language):
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_LOCATION)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(TEMPLATE_FILE_NAME)

    other_languages_buttons = generate_language_navigation_buttons(language)
    
    generated_note = f"This README file has been generated on {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}, {time.tzname}."

    return template.render(load_translation(language), other_languages_buttons=other_languages_buttons, generated_text=generated_note)

def generate_readme_files():
    for language in LANGUAGES:
        
        readme_content = render_readme_template(language)
        
        with open(f'README_{language}.md', 'w', encoding=ENCODING_FORMAT) as file:
            file.write(readme_content)

        if language == DEFAULT_LANGUAGE:
            with open(f'README.md', 'w', encoding=ENCODING_FORMAT) as file:
                file.write(readme_content)

def main():
    generate_readme_files()
    
    print('README files have been successfully generated!')
    
if __name__ == '__main__':
    main()