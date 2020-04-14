import os
import jinja2
from datetime import datetime

class Template:
    latex_jinja_env = None
    template = None

    def __init__(self, templates_path):
        self.latex_jinja_env = jinja2.Environment(
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
            loader=jinja2.FileSystemLoader(os.path.abspath(templates_path))
        )
        self.template = None


    def populate(self, output_prefix, output_dir='outputs'):
        raise NotImplementedError


    def generate_savepath(self, save_dir, prefix=''):
        timestamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S%p")
        savepath = os.path.join(save_dir, prefix + '_' + timestamp + '.tex')
        return savepath


class AnimalTemplate(Template):
    def __init__(self, templates_path='templates'):
        super(AnimalTemplate, self).__init__(templates_path)
        self.template = self.latex_jinja_env.get_template('animal.tex')


    def populate(self, output_prefix, output_dir='outputs'):
        result = self.template.render(
            # TODO
        )
        savepath = self.generate_savepath(output_dir, output_prefix)
        with open(savepath, 'w') as file: file.write(result)
        print('Latex generated at ' + savepath)


class PlantTemplate(Template):
    def __init__(self, templates_path='templates'):
        super(PlantTemplate, self).__init__(templates_path)
        self.template = self.latex_jinja_env.get_template('plant.tex')


    def populate(self, output_prefix, output_dir='outputs'):
        result = self.template.render(
            # TODO
        )
        savepath = self.generate_savepath(output_dir, output_prefix)
        with open(savepath, 'w') as file: file.write(result)
        print('Latex generated at ' + savepath)


class DemoTemplate(Template):
    def __init__(self, templates_path='templates'):
        super(DemoTemplate, self).__init__(templates_path)
        self.template = self.latex_jinja_env.get_template('demo.tex')


    def populate(self, output_prefix, output_dir='outputs'):
        result = self.template.render(
            name='Sayan'
        )
        savepath = self.generate_savepath(output_dir, output_prefix)
        with open(savepath, 'w') as file: file.write(result)
        print('Latex generated at ' + savepath)
