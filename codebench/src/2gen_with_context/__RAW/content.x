START
<ul>
    {% if users is defined %}
        {% for u in users2 -%}

        <li>
            {% set v1 = fn_x2(u.name) %}
            {{ v1 }}
            {% set v2 = fn_x2(u.name, "argument supplied from 'content.x'") %}
            {{ v2 }}
            {{ u.name | flt_x1}}
        </li>
        {% endfor -%}
    {% endif %}
</ul>
END


