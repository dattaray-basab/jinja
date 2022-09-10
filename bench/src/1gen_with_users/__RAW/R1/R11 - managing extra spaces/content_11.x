START
<ul>
    {%- for u in users %}
    <li>
        {% set v2 = fn_x2(u.name, "apply function with argument supplied from 'content_11.x'") %}
        {{- v2 | flt_x1 | trim }}
    </li>
    {%- endfor %}
</ul>
END

