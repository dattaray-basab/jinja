START
<ul>
    {% for u in users -%}
    <li>
        {% set v1 = fn_x2(u.name) %}
        {{ v1 }}
        {% set v2 = fn_x2(u.name, "argument supplied from 'content.x'") %}
        {{ v2 }}
        {{ u.name | flt_x1}}
    </li>
    {% endfor -%}
</ul>
END


