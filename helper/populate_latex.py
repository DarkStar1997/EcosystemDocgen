import os
import jinja2
from datetime import datetime

class Template:
    latex_jinja_env = None
    template = None
    data = None

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
        self.data = None


    def generate_savepath(self, save_dir, prefix=''):
        timestamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S%p")
        savepath = os.path.join(save_dir, prefix + '_' + timestamp + '.tex')
        return savepath


    def populate(self, output_prefix, output_dir='outputs'):
        if self.data and self.template:
            result = self.template.render(
                data=self.data
            )
            savepath = self.generate_savepath(output_dir, output_prefix)
            with open(savepath, 'w') as file: file.write(result)
            print('Latex generated at ' + savepath)


class AnimalTemplate(Template):
    def __init__(self, templates_path='templates', extra_data=None):
        super(AnimalTemplate, self).__init__(templates_path)
        self.template = self.latex_jinja_env.get_template('animal.tex')
        self.data = dict(
            AGE_DTH='img/AGE_DTH.png',
            FIT_DTH='img/FIT_DTH.png',
            AFR_DTH='img/AFR_DTH.png',
            MX_AGE='img/MX_AGE.png',
            POP='img/POP.png',
            M_POP='img/M_POP.png',
            M_AGE_START='img/M_AGE_START.png',
            M_AGE_END='img/M_AGE_END.png',
            C_PROB='img/C_PROB.png',
            MT_PROB='img/MT_PROB.png',
            OF_FACTOR='img/OF_FACTOR.png',
            X_ST='img/X_ST.png',
            X_VT='img/X_VT.png',
            X_SP='img/X_SP.png',
            X_AP='img/X_AP.png',
            AVG_GEN='img/AVG_GEN.png',
            AVG_AGE='img/AVG_AGE.png',
            AVG_HT='img/AVG_HT.png',
            AVG_WT='img/AVG_WT.png',
            AVG_SFIT='img/AVG_SFIT.png',
            AVG_IMM='img/AVG_IMM.png',
            AVG_DTHF='img/AVG_DTHF.png',
            AVGMA_SP='img/AVGMA_SP.png',
            AVGMA_AP='img/AVGMA_AP.png',
            AVGMA_ST='img/AVGMA_ST.png',
            AVGMA_VT='img/AVGMA_VT.png',
            AVG_VIS='img/AVG_VIS.png',
            TMB_HT='img/TMB_HT.png',
            TMB_WT='img/TMB_WT.png',
            TM_HT='img/TM_HT.png',
            TM_WT='img/TM_WT.png',
            TMB_SP='img/TMB_SP.png',
            TMB_AP='img/TMB_AP.png',
            TMB_ST='img/TMB_ST.png',
            TMB_VT='img/TMB_VT.png',
            TM_SP='img/TM_SP.png',
            TMM_SP='img/TMM_SP.png',
            TMM_ST='img/TMM_ST.png',
            TMM_VT='img/TMM_VT.png',
            TMM_HT='img/TMM_HT.png',
            TMM_WT='img/TMM_WT.png'
        )
        if extra_data:
            for k in extra_data: self.data[k] = extra_data[k]


class PlantTemplate(Template):
    def __init__(self, templates_path='templates', extra_data=None):
        super(PlantTemplate, self).__init__(templates_path)
        self.template = self.latex_jinja_env.get_template('plant.tex')
        self.data = dict(
            AGE_DTH='img/AGE_DTH.png',
            FIT_DTH='img/FIT_DTH.png',
            AFR_DTH='img/AFR_DTH.png',
            MX_AGE='img/MX_AGE.png',
            POP='img/POP.png',
            M_POP='img/M_POP.png',
            M_AGE_START='img/M_AGE_START.png',
            M_AGE_END='img/M_AGE_END.png',
            C_PROB='img/C_PROB.png',
            MT_PROB='img/MT_PROB.png',
            OF_FACTOR='img/OF_FACTOR.png',
            X_VT='img/X_VT.png',
            AVG_GEN='img/AVG_GEN.png',
            AVG_AGE='img/AVG_AGE.png',
            AVG_HT='img/AVG_HT.png',
            AVG_WT='img/AVG_WT.png',
            AVG_SFIT='img/AVG_SFIT.png',
            AVG_IMM='img/AVG_IMM.png',
            AVG_DTHF='img/AVG_DTHF.png',
            AVGMA_VT='img/AVGMA_VT.png',
            TMB_HT='img/TMB_HT.png',
            TMB_WT='img/TMB_WT.png',
            TM_HT='img/TM_HT.png',
            TM_WT='img/TM_WT.png',
            TMB_VT='img/TMB_VT.png',
            TMM_VT='img/TMM_VT.png',
            TMM_HT='img/TMM_HT.png',
            TMM_WT='img/TMM_WT.png'
        )
        if extra_data:
            for k in extra_data: self.data[k] = extra_data[k]


class DemoTemplate(Template):
    def __init__(self, templates_path='templates', extra_data=None):
        super(DemoTemplate, self).__init__(templates_path)
        self.template = self.latex_jinja_env.get_template('demo.tex')
        self.data = dict(
            name='Sayan',
            greeting='Byeee'
        )
        if extra_data:
            for k in extra_data: self.data[k] = extra_data[k]
