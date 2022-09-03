from jinja2 import Template

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Mazda', 'price': 16400},
    {'model': 'BMW', 'price': 49220},
    {'model': 'Volvo', 'price': 30999},
]


tpl = '''Суммарная цена автомобилей: ${{ cs | sum(attribute="price") }}
Марка автомобля с максимальной ценой: {{ (cs | max(attribute='price')).model }}
Марка автомобля с минимальной ценой: {{ (cs | min(attribute='price')).model }}
Случайный автомобиль: {{ (cs | random) }}
'''
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)


digs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tpl = 'Сумма цифр в digs: {{ d | sum }}'
tm = Template(tpl)
msg = tm.render(d=digs)
print(msg)

# подстановка фильтров
persons = [
    {'name': 'Alex', 'age': 18, 'weight': 78.5},
    {'name': 'Niko', 'age': 20, 'weight': 92.1},
    {'name': 'Ivan', 'age': 39, 'weight': 83.9}
]
tpl = '''
{%- for u in users -%}
{% filter upper %}{{ u.name }}{% endfilter %}
{% endfor -%}
'''
tm = Template(tpl)
msg = tm.render(users=persons)
print(msg)


html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type='{{ type }}' name='{{ name }}' value='{{ value | e }}' size='{{ size }}'>
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''

tm = Template(html)
msg = tm.render()
print(msg)


persons = [
    {'name': 'Alex', 'age': 18, 'weight': 78.5},
    {'name': 'Niko', 'age': 20, 'weight': 92.1},
    {'name': 'Ivan', 'age': 39, 'weight': 83.9}
]
html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{ u.name }} {{ caller(u) }}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
        <li>age: {{ user.age }}
        <li>weight: {{ user.weight }}
    </ul>
{% endcall -%}
'''
tm = Template(html)
msg = tm.render(users=persons)
print(msg)
