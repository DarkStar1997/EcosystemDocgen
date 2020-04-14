import matplotlib.pyplot as plt

class Organism:
    @classmethod
    def generate_graphs(cls, df, savepath='../outputs/img/'):
        cls.generate_mortality_graphs(df, savepath)
        cls.generate_demographic_graphs(df, savepath)
        cls.generate_copulation_graphs(df, savepath)
        cls.generate_dependency_graphs(df, savepath)
        cls.generate_average_graphs(df, savepath)
        cls.generate_theoretical_graphs(df, savepath)

    @classmethod
    def generate_mortality_graphs(cls, df, savepath):
        raise NotImplementedError

    @classmethod
    def generate_demographic_graphs(cls, df, savepath):
        raise NotImplementedError

    @classmethod
    def generate_copulation_graphs(cls, df, savepath):
        raise NotImplementedError

    @classmethod
    def generate_dependency_graphs(cls, df, savepath):
        raise NotImplementedError

    @classmethod
    def generate_average_graphs(cls, df, savepath):
        raise NotImplementedError

    @classmethod
    def generate_theoretical_graphs(cls, df, savepath):
        raise NotImplementedError


class Plant(Organism):
    @classmethod
    def generate_mortality_graphs(cls, df, savepath):
        """
            AGE_DTH
            FIT_DTH
            AFR_DTH
            MX_AGE
        """
        plt.suptitle('Age affecting Death')
        x = df.index
        y = df['AGE_DTH']
        plt.plot(x, y, '-r')
        plt.ylabel("Factor")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AGE_DTH.png')
        plt.clf()

        plt.suptitle('Fitness affecting Death')
        x = df.index
        y = df['FIT_DTH']
        plt.plot(x, y, '-b')
        plt.ylabel("Factor")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'FIT_DTH.png')
        plt.clf()

        plt.suptitle('Age vs. Fitness affecting Death')
        x = df.index
        y = df['AFR_DTH']
        plt.plot(x, y, '-b')
        plt.ylabel("Ratio")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AFR_DTH.png')
        plt.clf()

        plt.suptitle('Max age with time')
        x = df.index
        y = df['MX_AGE']
        plt.plot(x, y, '-b')
        plt.ylabel("Max age")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'MX_AGE.png')
        plt.clf()


    @classmethod
    def generate_demographic_graphs(cls, df, savepath):
        """
            POP
        """
        plt.suptitle('Population')
        x = df.index
        y = df['POP']
        plt.plot(x, y, '-b')
        plt.ylabel("Population")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'POP.png')
        plt.clf()


    @classmethod
    def generate_copulation_graphs(cls, df, savepath):
        """
            M_POP
            M_AGE_START
            M_AGE_END
            C_PROB
            MT_PROB
            OF_FACTOR
        """
        plt.suptitle('Matable population')
        x = df.index
        y = df['M_POP']
        plt.plot(x, y, '-r')
        plt.ylabel("Matable Population")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'M_POP.png')
        plt.clf()

        plt.suptitle('Mating Start')
        x = df.index
        y = df['M_AGE_START']
        plt.plot(x, y, '-b')
        plt.ylabel("Age")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'M_AGE_START.png')
        plt.clf()

        plt.suptitle('Mating End')
        x = df.index
        y = df['M_AGE_END']
        plt.plot(x, y, '-r')
        plt.ylabel("Age")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'M_AGE_END.png')
        plt.clf()

        plt.suptitle('Mutation')
        x = df.index
        y = df['MT_PROB']
        plt.plot(x, y, '-r')
        plt.ylabel("Probability")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'MT_PROB.png')
        plt.clf()

        plt.suptitle('Conceive')
        x = df.index
        y = df['C_PROB']
        plt.plot(x, y, '-b')
        plt.ylabel("Probability")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'C_PROB.png')
        plt.clf()

        plt.suptitle('Multiple offprings')
        x = df.index
        y = df['OF_FACTOR']
        plt.plot(x, y, '-b')
        plt.ylabel("Factor")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'OF_FACTOR.png')
        plt.clf()


    @classmethod
    def generate_dependency_graphs(cls, df, savepath):
        """
            HT_VT
            WT_VT
        """
        plt.suptitle('Factors affecting Vitality')
        x = df.index
        y = df['HT_VT']
        plt.plot(x, y, '-r', label='Height')
        x = df.index
        y = df['WT_VT']
        plt.plot(x, y, '-b', label='Weight')
        plt.ylabel("Factor")
        plt.legend(loc="upper right")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'X_VT.png')
        plt.clf()


    @classmethod
    def generate_average_graphs(cls, df, savepath):
        """
            AVG_GEN
            AVG_AGE
            AVG_HT
            AVG_WT
            AVG_SFIT
            AVG_IMM
            AVG_DTHF
            AVGMA_VT
        """
        plt.suptitle('Generation')
        x = df.index
        y = df['AVG_GEN']
        plt.plot(x, y, '-g')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_GEN.png')
        plt.clf()

        plt.suptitle('Age')
        x = df.index
        y = df['AVG_AGE']
        plt.plot(x, y, '-m')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_AGE.png')
        plt.clf()

        plt.suptitle('Height')
        x = df.index
        y = df['AVG_HT']
        plt.plot(x, y, '-b')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_HT.png')
        plt.clf()

        plt.suptitle('Weight')
        x = df.index
        y = df['AVG_WT']
        plt.plot(x, y, '-r')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_WT.png')
        plt.clf()

        plt.suptitle('Static Fitness')
        x = df.index
        y = df['AVG_SFIT']
        plt.plot(x, y, '-b')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_SFIT.png')
        plt.clf()

        plt.suptitle('Immunity')
        x = df.index
        y = df['AVG_IMM']
        plt.plot(x, y, '-r')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_IMM.png')
        plt.clf()

        plt.suptitle('Death Factor')
        x = df.index
        y = df['AVG_DTHF']
        plt.plot(x, y, '-m')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_DTHF.png')
        plt.clf()

        plt.suptitle('Max vitality at age')
        x = df.index
        y = df['AVGMA_VT']
        plt.plot(x, y, '-c')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVGMA_VT.png')
        plt.clf()


    @classmethod
    def generate_theoretical_graphs(cls, df, savepath):
        """
            TMB_HT
            TMB_WT
            TM_HT
            TM_WT
            TMB_VT
            TMM_VT
            TMM_HT
            TMM_WT
        """
        plt.suptitle('Max base height')
        x = df.index
        y = df['TMB_HT']
        plt.plot(x, y, '-b')
        plt.ylabel("meters")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMB_HT.png')
        plt.clf()

        plt.suptitle('Max height')
        x = df.index
        y = df['TM_HT']
        plt.plot(x, y, '-b')
        plt.ylabel("meters")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TM_HT.png')
        plt.clf()

        plt.suptitle('Max base weight')
        x = df.index
        y = df['TMB_WT']
        plt.plot(x, y, '-r')
        plt.ylabel("kg")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMB_WT.png')
        plt.clf()

        plt.suptitle('Max weight')
        x = df.index
        y = df['TM_WT']
        plt.plot(x, y, '-r')
        plt.ylabel("kg")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TM_WT.png')
        plt.clf()

        plt.suptitle('Max base vitality')
        x = df.index
        y = df['TMB_VT']
        plt.plot(x, y, '-g')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMB_VT.png')
        plt.clf()

        plt.suptitle('Max vitality multiplier')
        x = df.index
        y = df['TMM_VT']
        plt.plot(x, y, '-m')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMM_VT.png')
        plt.clf()

        plt.suptitle('Max height multiplier')
        x = df.index
        y = df['TMM_HT']
        plt.plot(x, y, '-r')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMM_HT.png')
        plt.clf()

        plt.suptitle('Max weight multiplier')
        x = df.index
        y = df['TMM_WT']
        plt.plot(x, y, '-b')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMM_WT.png')
        plt.clf()


class Animal(Organism):
    @classmethod
    def generate_mortality_graphs(cls, df, savepath):
        """
            AGE_DTH
            FIT_DTH
            AFR_DTH
            MX_AGE
        """
        plt.suptitle('Age affecting Death')
        x = df.index
        y = df['AGE_DTH']
        plt.plot(x, y, '-r')
        plt.ylabel("Factor")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AGE_DTH.png')
        plt.clf()

        plt.suptitle('Fitness affecting Death')
        x = df.index
        y = df['FIT_DTH']
        plt.plot(x, y, '-b')
        plt.ylabel("Factor")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'FIT_DTH.png')
        plt.clf()

        plt.suptitle('Age vs. Fitness affecting Death')
        x = df.index
        y = df['AFR_DTH']
        plt.plot(x, y, '-b')
        plt.ylabel("Ratio")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AFR_DTH.png')
        plt.clf()

        plt.suptitle('Max age with time')
        x = df.index
        y = df['MX_AGE']
        plt.plot(x, y, '-b')
        plt.ylabel("Max age")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'MX_AGE.png')
        plt.clf()


    @classmethod
    def generate_demographic_graphs(cls, df, savepath):
        """
            MALE
            FEMALE
        """

        plt.suptitle('Population')
        x = df.index
        y = df['MALE']
        plt.plot(x, y, '-b', label='Male')
        x = df.index
        y = df['FEMALE']
        plt.plot(x, y, '-r', label='Female')
        plt.ylabel("Population")
        plt.legend(loc="upper right")
        plt.yticks(rotation=45)

        plt.savefig(savepath + "POP.png")
        plt.clf()


    @classmethod
    def generate_copulation_graphs(cls, df, savepath):
        """
            M_MALE
            M_FEMALE
            M_AGE_START
            M_AGE_END
            C_PROB
            MT_PROB
            OF_FACTOR
        """

        plt.suptitle('Matable population')
        x = df.index
        y = df['M_MALE']
        plt.plot(x, y, '-b', label='Male')
        x = df.index
        y = df['M_FEMALE']
        plt.plot(x, y, '-r', label='Female')
        plt.ylabel("Matable Population")
        plt.legend(loc="upper right")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'M_POP.png')
        plt.clf()

        plt.suptitle('Mating Start')
        x = df.index
        y = df['M_AGE_START']
        plt.plot(x, y, '-b')
        plt.ylabel("Age")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'M_AGE_START.png')
        plt.clf()

        plt.suptitle('Mating End')
        x = df.index
        y = df['M_AGE_END']
        plt.plot(x, y, '-r')
        plt.ylabel("Age")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'M_AGE_END.png')
        plt.clf()

        plt.suptitle('Mutation')
        x = df.index
        y = df['MT_PROB']
        plt.plot(x, y, '-r')
        plt.ylabel("Probability")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'MT_PROB.png')
        plt.clf()

        plt.suptitle('Conceive')
        x = df.index
        y = df['C_PROB']
        plt.plot(x, y, '-b')
        plt.ylabel("Probability")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'C_PROB.png')
        plt.clf()

        plt.suptitle('Multiple offprings')
        x = df.index
        y = df['OF_FACTOR']
        plt.plot(x, y, '-b')
        plt.ylabel("Factor")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'OF_FACTOR.png')
        plt.clf()


    @classmethod
    def generate_dependency_graphs(cls, df, savepath):
        """
            HT_ST
            WT_ST
            HT_VT
            WT_VT
            HT_SP
            WT_SP
            ST_SP
            VT_SP
            VT_AP
            ST_AP
        """
        plt.suptitle('Factors affecting Stamina')
        x = df.index
        y = df['HT_ST']
        plt.plot(x, y, '-r', label='Height')
        x = df.index
        y = df['WT_ST']
        plt.plot(x, y, '-b', label='Weight')
        plt.ylabel("Factor")
        plt.legend(loc="upper right")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'X_ST.png')
        plt.clf()

        plt.suptitle('Factors affecting Vitality')
        x = df.index
        y = df['HT_VT']
        plt.plot(x, y, '-r', label='Height')
        x = df.index
        y = df['WT_VT']
        plt.plot(x, y, '-b', label='Weight')
        plt.ylabel("Factor")
        plt.legend(loc="upper right")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'X_VT.png')
        plt.clf()

        plt.suptitle('Factors affecting Speed')
        x = df.index
        y = df['HT_SP']
        plt.plot(x, y, '-r', label='Height')
        x = df.index
        y = df['WT_SP']
        plt.plot(x, y, '-b', label='Weight')
        x = df.index
        y = df['ST_SP']
        plt.plot(x, y, '-c', label='Stamina')
        x = df.index
        y = df['VT_SP']
        plt.plot(x, y, '-g', label='Vitality')
        plt.ylabel("Factor")
        plt.legend(loc="upper right")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'X_SP.png')
        plt.clf()

        plt.suptitle('Factors affecting Appetite')
        x = df.index
        y = df['VT_AP']
        plt.plot(x, y, '-g', label='Vitality')
        x = df.index
        y = df['ST_AP']
        plt.plot(x, y, '-c', label='Stamina')
        plt.ylabel("Factor")
        plt.legend(loc="upper right")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'X_AP.png')
        plt.clf()


    @classmethod
    def generate_average_graphs(cls, df, savepath):
        """
            AVG_GEN
            AVG_AGE
            AVG_HT
            AVG_WT
            AVG_SFIT
            AVG_IMM
            AVG_DTHF
            AVGMA_SP
            AVGMA_AP
            AVGMA_ST
            AVGMA_VT
            AVG_VIS
        """
        plt.suptitle('Generation')
        x = df.index
        y = df['AVG_GEN']
        plt.plot(x, y, '-g')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_GEN.png')
        plt.clf()

        plt.suptitle('Age')
        x = df.index
        y = df['AVG_AGE']
        plt.plot(x, y, '-m')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_AGE.png')
        plt.clf()

        plt.suptitle('Height')
        x = df.index
        y = df['AVG_HT']
        plt.plot(x, y, '-b')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_HT.png')
        plt.clf()

        plt.suptitle('Weight')
        x = df.index
        y = df['AVG_WT']
        plt.plot(x, y, '-r')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_WT.png')
        plt.clf()

        plt.suptitle('Static Fitness')
        x = df.index
        y = df['AVG_SFIT']
        plt.plot(x, y, '-b')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_SFIT.png')
        plt.clf()

        plt.suptitle('Immunity')
        x = df.index
        y = df['AVG_IMM']
        plt.plot(x, y, '-r')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_IMM.png')
        plt.clf()

        plt.suptitle('Death Factor')
        x = df.index
        y = df['AVG_DTHF']
        plt.plot(x, y, '-m')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_DTHF.png')
        plt.clf()

        plt.suptitle('Max speed at age')
        x = df.index
        y = df['AVGMA_SP']
        plt.plot(x, y, '-g')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVGMA_SP.png')
        plt.clf()

        plt.suptitle('Max appetite at age')
        x = df.index
        y = df['AVGMA_AP']
        plt.plot(x, y, '-b')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVGMA_AP.png')
        plt.clf()

        plt.suptitle('Max stamina at age')
        x = df.index
        y = df['AVGMA_ST']
        plt.plot(x, y, '-r')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVGMA_ST.png')
        plt.clf()

        plt.suptitle('Max vitality at age')
        x = df.index
        y = df['AVGMA_VT']
        plt.plot(x, y, '-c')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVGMA_VT.png')
        plt.clf()

        plt.suptitle('Max vision radius')
        x = df.index
        y = df['AVG_VIS']
        plt.plot(x, y, '-m')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'AVG_VIS.png')
        plt.clf()


    @classmethod
    def generate_theoretical_graphs(cls, df, savepath):
        """
            TMB_HT
            TMB_WT
            TM_HT
            TM_WT
            TMB_SP
            TMB_AP
            TMB_ST
            TMB_VT
            TM_SP
            TMM_SP
            TMM_ST
            TMM_VT
            TMM_HT
            TMM_WT
        """
        plt.suptitle('Max base height')
        x = df.index
        y = df['TMB_HT']
        plt.plot(x, y, '-b')
        plt.ylabel("meters")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMB_HT.png')
        plt.clf()

        plt.suptitle('Max height')
        x = df.index
        y = df['TM_HT']
        plt.plot(x, y, '-b')
        plt.ylabel("meters")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TM_HT.png')
        plt.clf()

        plt.suptitle('Max base weight')
        x = df.index
        y = df['TMB_WT']
        plt.plot(x, y, '-r')
        plt.ylabel("kg")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMB_WT.png')
        plt.clf()

        plt.suptitle('Max weight')
        x = df.index
        y = df['TM_WT']
        plt.plot(x, y, '-r')
        plt.ylabel("kg")
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TM_WT.png')
        plt.clf()

        plt.suptitle('Max base speed')
        x = df.index
        y = df['TMB_SP']
        plt.plot(x, y, '-b')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMB_SP.png')
        plt.clf()

        plt.suptitle('Max base appetite')
        x = df.index
        y = df['TMB_AP']
        plt.plot(x, y, '-r')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMB_AP.png')
        plt.clf()

        plt.suptitle('Max base stamina')
        x = df.index
        y = df['TMB_ST']
        plt.plot(x, y, '-c')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMB_ST.png')
        plt.clf()

        plt.suptitle('Max base vitality')
        x = df.index
        y = df['TMB_VT']
        plt.plot(x, y, '-g')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMB_VT.png')
        plt.clf()

        plt.suptitle('Max speed')
        x = df.index
        y = df['TM_SP']
        plt.plot(x, y, '-b')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TM_SP.png')
        plt.clf()

        plt.suptitle('Max speed multiplier')
        x = df.index
        y = df['TMM_SP']
        plt.plot(x, y, '-g')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMM_SP.png')
        plt.clf()

        plt.suptitle('Max stamina multiplier')
        x = df.index
        y = df['TMM_ST']
        plt.plot(x, y, '-c')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMM_ST.png')
        plt.clf()

        plt.suptitle('Max vitality multiplier')
        x = df.index
        y = df['TMM_VT']
        plt.plot(x, y, '-m')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMM_VT.png')
        plt.clf()

        plt.suptitle('Max height multiplier')
        x = df.index
        y = df['TMM_HT']
        plt.plot(x, y, '-r')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMM_HT.png')
        plt.clf()

        plt.suptitle('Max weight multiplier')
        x = df.index
        y = df['TMM_WT']
        plt.plot(x, y, '-b')
        plt.yticks(rotation=45)

        plt.savefig(savepath + 'TMM_WT.png')
        plt.clf()
