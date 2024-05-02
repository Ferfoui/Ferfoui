import jinja2
import json

LANGUAGES_LOCATION = 'code/languages/'
TEMPLATES_LOCATION = 'code/templates/'

LANGUAGES = ['EN', 'FR']

def load_translation(language: str):
    with open(f"{LANGUAGES_LOCATION}{language.upper()}.json", 'r', encoding='utf-8') as file:
        return json.load(file)

def render_readme_template(language):
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_LOCATION)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('README.md.j2')
    
    other_languages_buttons = generate_language_navigation_buttons(language)

    return template.render(load_translation(language), other_languages_buttons=other_languages_buttons)

def generate_language_navigation_buttons(current_language):
    buttons = ''
    for language in LANGUAGES:
        
        if language.lower() == current_language.lower():
            continue
        
        buttons += f'[![{language}](https://img.shields.io/badge/{language}-blue)](https://github.com/Ferfoui/Ferfoui/blob/main/README_{language}.md)  '
    
    return buttons

def generate_readme_files():
    for language in LANGUAGES:
        
        readme_content = render_readme_template(language)
        
        with open(f'README_{language}.md', 'w', encoding='utf-8') as file:
            file.write(readme_content)
        
        if language == 'EN':
            with open(f'README.md', 'w', encoding='utf-8') as file:
                file.write(readme_content)

def main():
    generate_readme_files()
    
    print('README.md generated successfully!')
    
if __name__ == '__main__':
    main()