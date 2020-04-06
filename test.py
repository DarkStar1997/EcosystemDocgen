import os
import jinja2

latex_jinja_env = jinja2.Environment(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%-',
    line_comment_prefix='%#',
    trim_blocks=True,
    autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.abspath('templates'))
)

template = latex_jinja_env.get_template('demo.tex')
result = template.render(name='Sayan')
with open('outputs/dd.tex', 'w') as file: file.write(result)