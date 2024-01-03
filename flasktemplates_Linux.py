import sys
import os

def create_folder_structure(base_folder):
    static_folder = os.path.join(base_folder, 'static')
    img_folder = os.path.join(static_folder, 'img')
    templates_folder = os.path.join(base_folder, 'templates')

    # Создаем папки, если они не существуют
    os.makedirs(static_folder, exist_ok=True)
    os.makedirs(img_folder, exist_ok=True)
    os.makedirs(templates_folder, exist_ok=True)

    # Создаем файлы, если они не существуют
    styles_file = os.path.join(static_folder, 'styles.css')
    base_html_file = os.path.join(templates_folder, 'base.html')
    index_html_file = os.path.join(templates_folder, 'index.html')
    main_py_file = os.path.join(base_folder, 'main.py')

    # Создаем пустые файлы, если они не существуют
    open(styles_file, 'a').close()
    open(base_html_file, 'a').close()
    open(index_html_file, 'a').close()
    open(main_py_file, 'a').close()

    # Записываем базовую структуру Flask проекта в файл main.py
    with open(main_py_file, 'w') as main_file:
        main_file.write("""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
""")

    # Записываем содержимое base.html
    with open(base_html_file, 'w') as base_html:
        base_html.write("""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    {% block title %}{% endblock %}
</head>
<body>
    {% block body %}{% endblock %}
</body>
</html>
""")

    # Записываем содержимое index.html
    with open(index_html_file, 'w') as index_html:
        index_html.write("""
{% extends 'base.html' %}
{% block title %}
<title></title>
{% endblock %}

{% block body %}{% endblock %}
""")

def folder_exists(folder_path):
    return os.path.exists(folder_path)

def get_folder_path():
    if len(sys.argv) < 2:
        print("Пplease run the application via the console as: flasktemplates path/to/you/project/folder")
        sys.exit(1)

    folder_path = sys.argv[1]
    return folder_path

if __name__ == "__main__":
    folder = get_folder_path()

    if folder_exists(folder):
        print(f"please wait!")
        create_folder_structure(folder)
        print(f"The flask project structure is created in '{folder}'")
    else:
        print(f"Folder '{folder}' does not exist. Check if you specified it correctly.")