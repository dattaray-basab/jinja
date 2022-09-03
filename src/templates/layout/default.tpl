<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}
    Блок контента
        {% block table_contents %}
        <ul>
        {% for li in list_table -%}
        <li>{% block item scoped %}{{ li }}{% endblock item %}</li>
        {% endfor -%}
        </ul>
        {% endblock table_contents %}
    {% endblock content %}
</body>
</html>