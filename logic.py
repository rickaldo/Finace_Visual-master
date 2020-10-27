import pandas as pd


class Logic:

    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(self.path, sep=";")
        self.betrag = self.df['Betrag']
        self.saldo = self.df['Saldo']
        self.kategorie = self.df['Kategorie']
        self.setTypes()

    def setTypes(self):
        self.betrag = self.betrag.str.replace(".", "")
        self.betrag = self.betrag.str.replace(",", ".")
        self.betrag = self.betrag.astype("float")

        self.saldo = self.saldo.str.replace(".", "")
        self.saldo = self.saldo.str.replace(",", ".")
        self.saldo = self.saldo.astype("float")

    def getCategories(self):

        ################################ Categories ########################################

        freetime = self.betrag.where(self.kategorie.str.contains('Freizeit')).sum() 
        dwell = self.betrag.where(self.kategorie.str.contains('Wohnen')).sum() 
        union = self.betrag.where(self.kategorie.str.contains('Gewerkschaft')).sum() 
        food = self.betrag.where(self.kategorie.str.contains('Lebensmittel')).sum() 
        savings = self.betrag.where(self.kategorie.str.contains('Sparen')).sum() 
        car = self.betrag.where(self.kategorie.str.contains('Auto')).sum() 
        college = extra = self.betrag.where(self.kategorie.str.contains('Uni')).sum()

        income = (self.getSubCategories()['mama'] + self.getSubCategories()['papa'] + self.getSubCategories()['oma']
                + self.getSubCategories()['salary'] + self.getSubCategories()['sellshares'] 
                + self.getSubCategories()['selling']) 

        income_from_savings = self.getSubCategories()['save']
        
        dict = {
            'freetime': freetime *-1,
            'dwell': dwell *-1,
            'union': union *-1,
            'food': food *-1,
            'savings': savings *-1,
            'car': car *-1,
            'income': income,
            'college': college *-1,
            'income_from_savings': income_from_savings *-1,
        }

        #print (dict)
        return dict

    def getSubCategories(self):

        ############################### Sub-Categories ####################################

        rent = self.betrag.where(self.kategorie.str.contains('Miete')).sum()
        electricity = self.betrag.where(self.kategorie.str.contains('Strom')).sum()
        internet = self.betrag.where(self.kategorie.str.contains('Internet')).sum()
        gez = self.betrag.where(self.kategorie.str.contains('Rundfunk')).sum()

        fitness = self.betrag.where(self.kategorie.str.contains('Fitness')).sum()
        gaming = self.betrag.where(self.kategorie.str.contains('Zocken')).sum()
        casino = self.betrag.where(self.kategorie.str.contains('Casino')).sum()
        entertainment = self.betrag.where(self.kategorie.str.contains('Entertainment')).sum()
        shisha = self.betrag.where(self.kategorie.str.contains('Shisha')).sum()
        cash = self.betrag.where(self.kategorie.str.contains('Bargeld')).sum()
        football = self.betrag.where(self.kategorie.str.contains('Fußball')).sum()
        party = self.betrag.where(self.kategorie.str.contains('Feiern')).sum()
        extra = self.betrag.where(self.kategorie.str.contains('Extra')).sum()
        clothings = self.betrag.where(self.kategorie.str.contains('Klamotten')).sum()

        fastfood = self.betrag.where(self.kategorie.str.contains('Fast')).sum()
        normalfood = self.betrag.where(self.kategorie.str.contains('Normal')).sum()

        savingbook = self.betrag.where(self.kategorie.str.contains('Sparbuch')).sum()
        change = self.betrag.where(self.kategorie.str.contains('Kleingeld')).sum()
        buyshares = self.betrag.where(self.kategorie.str.contains('Sparen,Aktien')).sum()

        mama = self.betrag.where(self.kategorie.str.contains('Mama')).sum()
        papa = self.betrag.where(self.kategorie.str.contains('Papa')).sum()
        salary = self.betrag.where(self.kategorie.str.contains('Gehalt')).sum()
        save = self.betrag.where(self.kategorie.str.contains('Einnahmen,Spar')).sum()
        sellshares = self.betrag.where(self.kategorie.str.contains('Einnahmen,Aktien')).sum()
        selling = self.betrag.where(self.kategorie.str.contains('Verkauf')).sum()
        oma = self.betrag.where(self.kategorie.str.contains('Oma')).sum()

        refuel = self.betrag.where(self.kategorie.str.contains('Tanken')).sum()
        adac = self.betrag.where(self.kategorie.str.contains('ADAC')).sum()


        dict = {
            'rent': rent *-1 , 'electricity': electricity*-1,
            'internet': internet *-1, 'gez': gez*-1,
            'fitness': fitness*-1, 'gaming': gaming*-1,
            'casino': casino*-1, 'entertainment': entertainment*-1,
            'shisha': shisha*-1, 'cash': cash*-1,
            'football': football*-1, 'party': party*-1,
            'extra': extra*-1, 'fastfood': fastfood*-1,
            'normalfood': normalfood*-1, 'savingbook': savingbook*-1,
            'change': change*-1, 'buyshares': buyshares*-1,
            'mama': mama, 'papa': papa,
            'salary': salary, 'save': save*-1,
            'sellshares': sellshares, 'selling': selling*-1,
            'refuel': refuel*-1, 'adac': adac*-1,
            'oma': oma, 'clothings': clothings*-1,
        }

        #print (dict)

        return dict
