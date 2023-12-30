html_input = '<img src="/guide-media/01HB2XG9F28D5C608C40PXJNNX" alt="Keep-Only-Part-of-Clip-transcript-02.png">'

split_html = html_input.split("alt")

print(split_html)


default_url = "/URL"
default_alt = "FILENAME"

html_code = f'<a href="{default_url}" data-fancybox="lightbox" data-caption="">\n'
html_code += f'<img src="{default_url}" alt="{default_alt}" />\n'
html_code += '</a>'
# comment here
print(html_code)

print(html_input)