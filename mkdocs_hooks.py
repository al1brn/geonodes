import re
import posixpath

GEOMETRY_URL = "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/"
SHADER_URL = "https://docs.blender.org/manual/en/latest/render/shader_nodes/"


def class_to_page(name: str) -> str:
    # GreasePencil -> grease_pencil
    slug = re.sub(r"(?<!^)([A-Z])", r"_\1", name).lower()
    return f"{slug}.md"


def on_page_content(html, **kwargs):

    # Detect class anchor, e.g. "geonodes.core.treeclass.Tree"
    m = re.search(r'id="([A-Za-z0-9_.]+\.[A-Z][A-Za-z0-9_]*)"', html)
    class_anchor = m.group(1) if m else None

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
    
    # <#Name> -> link to current class anchor
    def repl_anchor(match):
        label = match.group(1).strip()

        if not class_anchor:
            return label  # fallback if not found

        return f'<a href="#{class_anchor}.{label}">{label}</a>'

    html = re.sub(r"&lt;&amp;Node (.*?)&gt;", repl_node, html)
    html = re.sub(r"&lt;&amp;ShaderNode (.*?)&gt;", repl_shader, html)
    html = re.sub(r"&lt;!(.*?)&gt;", repl_class, html)
    html = re.sub(r"&lt;#(.*?)&gt;", repl_anchor, html)

    return html

def on_page_markdown(markdown, page, **kwargs):

    def rel_link(from_url: str, to_url: str) -> str:
        from_dir = posixpath.dirname(from_url.rstrip("/"))
        return posixpath.relpath(to_url, start=from_dir or ".")    

    def repl_class(match):
        label = match.group(1).strip()

        #href = rel_link(page.url, class_to_page(label))
        target = f"api/{class_to_page(label)}"
        href = rel_link(page.file.src_uri, target)        

        return f"[{label}]({href})"

    markdown = re.sub(r"<!([A-Za-z_][A-Za-z0-9_]*)>", repl_class, markdown)
    return markdown
