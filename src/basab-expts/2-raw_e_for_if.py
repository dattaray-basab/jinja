from jinja2 import Template
from markupsafe import escape

# всё что внутри тегов raw endraw не будет изменено
data_raw = '''{% raw %}
    Модуль Jinja вместо определения {{ name }}
    подставляет соответствующее значение
    {% endraw %}
'''

data_link = '''В HTML-документе ссылки определеяются так:
<a href='#'>Ссылка</a>'''
# е - флаг экранирования специальных символов, которые браузер воспринимает как теги
tm = Template("{{ data_link | e }}")
msg = tm.render(data_link=data_link)
msg_escape = escape(data_link)  # аналогичный результат + более быстрый
print(f"msg == msg_escape - {msg == msg_escape}")

cities = [
    {'id': 1, 'city': 'Moscow'},
    {'id': 4, 'city': 'London'},
    {'id': 11, 'city': 'Kiev'},
    {'id': 46, 'city': 'New-York'},
    {'id': 59, 'city': 'Tokio'},
]

cities_text = '''<select name='cities'>
{% for c in cities -%}
{% if c.id > 20 -%}
    <option value='{{ c['id'] }}'>{{ c['city'] }}</option>
{% elif c.city == 'Moscow' -%}
    <option>{{ c['city'] }}</option>
{% else -%}
    {{ c['city'] }}
{% endif -%}
{% endfor -%}
</select>
'''
# {%- value -%} - минусы убирают переносы строки спереди или сзади. смотря где стоят

tm = Template(cities_text)
msg = tm.render(cities=cities)

print(msg)
