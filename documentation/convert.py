import os
import sys
import markdown as md
from bs4 import BeautifulSoup

def convert(filename):
    f = open(sys.argv[1]+"/"+filename+".md","r")
    md_file = f.read()
    f.close()

    html_body = md.markdown(md_file)
    appended = """<section class="vscode-light">\n""" + html_body + """\n</section>"""
    body = BeautifulSoup(appended, "html.parser")

    tf = open(sys.argv[1]+"/template.html","r")
    template = tf.read()
    tf.close()

    t = BeautifulSoup(template, "html.parser")
    t.body.append(body)

    op_file = open(sys.argv[1]+"/"+filename+".html", "w")
    op_file.write(str(t))
    op_file.close()

files = os.listdir(sys.argv[1])

md_files=[]
for f in files:
    if f.endswith('md'):
        md_files.append(f[:-3])

for f in md_files:
    convert(f)
