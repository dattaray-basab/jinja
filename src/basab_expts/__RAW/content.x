START
<ul>
    {% for u in users -%}
    <li>
        {% set v1 = fn_x2(u.name, '%% ') %}
        {{ v1 }}
        {{ u.name | flt_x1}}
    </li>
    {% endfor -%}
</ul>
END


