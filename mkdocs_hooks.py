import re

GEOMETRY_URL = "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/"
SHADER_URL = "https://docs.blender.org/manual/en/latest/render/shader_nodes/"


def class_to_page(name: str) -> str:
    # GreasePencil -> grease_pencil
    slug = re.sub(r"(?<!^)([A-Z])", r"_\1", name).lower()
    return f"{slug}.md"


def on_page_content(html, **kwargs):
    # <&Node Foo> -> link to Blender Geometry Nodes docs
    def repl_node(match):
        label = match.group(1)
        return f'<a href="{GEOMETRY_URL}">{label}</a>'

    # <&ShaderNode Foo> -> link to Blender Shader Nodes docs
    def repl_shader(match):
        label = match.group(1)
        return f'<a href="{SHADER_URL}">{label}</a>'

    # <!Vector> -> [Vector](vector.md)
    def repl_class(match):
        label = match.group(1)
        href = class_to_page(label)
        return f'<a href="{href}">{label}</a>'

    html = re.sub(r"&lt;&amp;Node (.*?)&gt;", repl_node, html)
    html = re.sub(r"&lt;&amp;ShaderNode (.*?)&gt;", repl_shader, html)
    html = re.sub(r"&lt;!(.*?)&gt;", repl_class, html)

    return html