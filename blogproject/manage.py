#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from bs4 import BeautifulSoup
from django.utils.safestring import SafeText

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    

# content = '&lt;font color="#000000" style="background-color: rgb(0, 0, 0);"&gt;asdfsadfsd&lt;/font&gt;&lt;font color="#000000" style=""&gt;&nbsp; &nbsp;&lt;/font&gt;&lt;font color="#9c00ff"&gt;asdlfjkasld&lt;/font&gt;'
# soup = BeautifulSoup(content, 'html.parser')
# for font_tag in soup.find_all('font'):
#     color = font_tag.get('color')
#     style = font_tag.get('style')
#     if color or style:
#         new_tag = soup.new_tag('span', style=f'color: {color};background-color:{style}')
#         new_tag.string = font_tag.string
#         font_tag.replace_with(new_tag)

# print(str(soup))