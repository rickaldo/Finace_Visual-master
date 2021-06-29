import matplotlib.pyplot as plt
import numpy as np

class Vision:
    def __init__(self, data):
        self.data = data
        
    def get_months(self):
        return ['Januar', 'Februar', 'März', 'April',
                       'Mai', 'Juni', 'Juli','August','September','August']

    def year_categorie_pie(self):
        dwell = sum(Categorieprep.dwell(self.data))
        union = sum(Categorieprep.union(self.data))
        food = sum(Categorieprep.food(self.data))
        savings = sum(Categorieprep.savings(self.data))
        car = sum(Categorieprep.car(self.data))
        freetime = sum(Categorieprep.freetime(self.data))

        sizes = [dwell, union, food, savings, car, freetime]
        labels = ['Miete', 'Gewerkschaft', 'Essen', 'Sparen', 'Auto', 'Freizeit']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.show()

    def month_categorie_pie(self, month):
        dwell = Categorieprep.dwell(self.data)[month]
        union = Categorieprep.union(self.data)[month]
        food = Categorieprep.food(self.data)[month]
        savings = Categorieprep.savings(self.data)[month]
        car = Categorieprep.car(self.data)[month]
        freetime = Categorieprep.freetime(self.data)[month]

        sizes = [dwell, union, food, savings, car, freetime]
        labels = ['Miete', 'Gewerkschaft', 'Essen', 'Sparen', 'Auto', 'Freizeit']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.show()

    def year_basic_chart(self):
        dwell = [a * -1 for a in Categorieprep.dwell(self.data)]
        union = [a * -1 for a in Categorieprep.union(self.data)]
        food = [a * -1 for a in Categorieprep.food(self.data)]
        savings = [a * -1 for a in Categorieprep.savings(self.data)]
        car = [a * -1 for a in Categorieprep.car(self.data)]
        freetime = [a * -1 for a in Categorieprep.freetime(self.data)]
        income_from_savings = SubCategorieprep.income_from_savings(self.data)
        income = Categorieprep.income(self.data)
        college = [a * -1 for a in SubCategorieprep.college(self.data)]
        
        x = Vision.get_months(self)
        y = np.vstack([dwell, union, food, savings, car, freetime, college])#, income_from_savings, income])
        label = ['Wohnungskosten','Gewerkschaft','Lebensmittel','Sparen','Auto','Freizeit','College']#,'Geld vom Sparbuch','Einkommen']
        
        fig,ax = plt.subplots(2,1) 
        ax[0].stackplot(x,dwell, union, food, savings, car, freetime, college,labels = label)
        ax[0].plot(income,label = 'Einkommen')
        ax[0].fill_between(x, 0, income, where = np.array(income) > 0, color='green', alpha=.25, interpolate=True)
        ax[0].set_title('Monatliche Kontobewegungen')
        ax[0].set_ylabel('€')
        ax[0].axhline(linewidth=3 , color = 'black')
        fig.legend(loc='upper left')

        all_spendings = [a + b + c + d + e + f for a,b,c,d,e,f in zip(dwell,union,food,college,car,freetime)]
        
        month_kpi = [h + g for h,g in zip(income,all_spendings)]

        ax[1].plot(x, month_kpi)
        plt.fill_between(x, 0, month_kpi, where = np.array(month_kpi) > 0, color='green', alpha=.25, interpolate=True)
        plt.fill_between(x, 0, month_kpi, where = np.array(month_kpi) < 0, color='red', alpha=.25 , interpolate=True)
        ax[1].set_title("Monatlicher Gewinn / Verlust")
        ax[1].set_ylabel('€')
        plt.show()
        
    def year_football_chart(self):
        football = SubCategorieprep.football(self.data)
        x = Vision.get_months(self)

        plt.plot(x, football)
        plt.title("Fußball Ausgaben")
        plt.fill_between(x, 0, football, where = np.array(football) > 0, alpha=.25 , interpolate=True)
        plt.show()

    def month_subcategorie_pie(self, categorie,month):
        if len(categorie) != 0:
            if categorie == 'freetime':
                fitness = SubCategorieprep.fitness(self.data)[month]
                gaming = SubCategorieprep.gaming(self.data)[month]
                cars = SubCategorieprep.cars(self.data)[month]
                entertain = SubCategorieprep.entertainment(self.data)[month]
                football = SubCategorieprep.football(self.data)[month]
                cash = SubCategorieprep.cash(self.data)[month]
                football = SubCategorieprep.football(self.data)[month]
                party = SubCategorieprep.party(self.data)[month]
                extra = SubCategorieprep.extra(self.data)[month]
                clothing = SubCategorieprep.clothing(self.data)[month] 

                sizes = [fitness, gaming, cars, entertain,
                         football, cash, football, party, extra, clothing]

                labels = ['Fitness', 'Zocken', 'Cars', 'Unterhaltungsmedien', 'Fußball',
                          'Bargeld', 'Fußball', 'Feiern', 'Extra','Kleidung']

                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                plt.title('Freizeit')
                plt.legend()
                plt.show()

                return sizes

            elif categorie == 'dwell':
                rent = SubCategorieprep.rent(self.data)[month]
                elec = SubCategorieprep.electricity(self.data)[month]
                internet = SubCategorieprep.internet(self.data)[month]
                gez = SubCategorieprep.gez(self.data)[month]

                sizes = [rent, elec, internet, gez]
                labels = ['Miete', 'Strom', 'Internet', 'Rundfunk']

                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                plt.title('Wohnen')
                plt.legend()
                plt.show()

                return sizes

            elif categorie == 'food':
                fast = SubCategorieprep.fastfood(self.data)[month]
                normal = SubCategorieprep.normalfood(self.data)[month]

                sizes = [fast, normal]
                labels = ['Fastfood', 'Supermarkt']

                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                plt.title('Lebensmittel')
                plt.legend()
                plt.show()

                return sizes

            elif categorie == 'savings':
                saving = SubCategorieprep.savingbook(self.data)[month]
                change = SubCategorieprep.change(self.data)[month]
                buy = SubCategorieprep.change(self.data)[month]

                sizes =[saving, change, buy]
                labels = ['Sparbuch', 'Kleingeld', 'Aktienkauf']

                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                plt.title('Sparen')
                plt.legend()
                plt.show()

                return sizes

            elif categorie == 'income':
                mama = SubCategorieprep.mama(self.data)[month]
                papa = SubCategorieprep.papa(self.data)[month]
                salary = SubCategorieprep.salary(self.data)[month]
                save = SubCategorieprep.save(self.data)[month]
                sellshares = SubCategorieprep.sellshares(self.data)[month]
                selling = SubCategorieprep.selling(self.data)[month]
                oma = SubCategorieprep.oma(self.data)[month]

                sizes = [mama, papa, salary, save, sellshares, selling,oma]
                labels = ['Mama', 'Papa', 'Gehalt', 'Sparbuch', 'Aktien verkauf', 'Verkauf','Oma']

                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                plt.title('Freizeit')
                plt.legend()
                plt.show()

                return sizes
            else:
                print('Ihre Antwort entspricht nicht den Kategorien.')
                print('Mögliche Kategorien: freetime; dwell; food; savings; income')
                cate = input('Geben Sie die Kategorie erneut ein: ')
                self.month_subcategorie_pie(cate,month)
        else:
            print('Keine Categorie eingegeben')
            cate = input('Geben Sie die Kategorie erneut ein: ')
            self.month_subcategorie_pie(cate,month)

        

class Categorieprep:
    @staticmethod
    def freetime(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. Categories'.format(i + 1)]['freetime'])
        return neededdata

    @staticmethod
    def dwell(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. Categories'.format(i + 1)]['dwell'])
        return neededdata

    @staticmethod
    def union(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. Categories'.format(i + 1)]['union'])
        return neededdata

    @staticmethod
    def food(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. Categories'.format(i + 1)]['food'])
        return neededdata

    @staticmethod
    def savings(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. Categories'.format(i + 1)]['savings'])
        return neededdata

    @staticmethod
    def car(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. Categories'.format(i + 1)]['car'])
        return neededdata

    @staticmethod
    def income(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. Categories'.format(i + 1)]['income'])
        return neededdata


class SubCategorieprep:
    @staticmethod
    def rent(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['rent'])
        return neededdata

    @staticmethod
    def electricity(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['electricity'])
        return neededdata

    @staticmethod
    def internet(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['internet'])
        return neededdata

    @staticmethod
    def gez(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['gez'])
        return neededdata

    @staticmethod
    def fitness(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['fitness'])
        return neededdata

    @staticmethod
    def gaming(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['gaming'])
        return neededdata

    @staticmethod
    def cars(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['car'])
        return neededdata

    @staticmethod
    def entertainment(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['entertainment'])
        return neededdata

    @staticmethod
    def football(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['football'])
        return neededdata

    @staticmethod
    def cash(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['cash'])
        return neededdata

    @staticmethod
    def football(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['football'])
        return neededdata

    @staticmethod
    def party(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['party'])
        return neededdata

    @staticmethod
    def extra(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['extra'])
        return neededdata

    @staticmethod
    def fastfood(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['fastfood'])
        return neededdata

    @staticmethod
    def normalfood(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['normalfood'])
        return neededdata

    @staticmethod
    def savingbook(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['savingbook'])
        return neededdata

    @staticmethod
    def change(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['change'])
        return neededdata

    @staticmethod
    def buyshares(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['buyshares'])
        return neededdata

    @staticmethod
    def mama(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['mama'])
        return neededdata

    @staticmethod
    def papa(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['papa'])
        return neededdata

    @staticmethod
    def salary(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['salary'])
        return neededdata

    @staticmethod
    def save(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['save'])
        return neededdata

    @staticmethod
    def sellshares(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['sellshares'])
        return neededdata

    @staticmethod
    def selling(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['selling'])
        return neededdata

    @staticmethod
    def refuel(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['refuel'])
        return neededdata

    @staticmethod
    def adac(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['adac'])
        return neededdata

    @staticmethod
    def oma(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['oma'])
        return neededdata

    @staticmethod
    def clothing(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. SubCategories'.format(i + 1)]['clothing'])
        return neededdata

    @staticmethod
    def college(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. Categories'.format(i + 1)]['college'])
        return neededdata
    
    @staticmethod
    def income_from_savings(data):
        neededdata = []
        for i in range(len(data)):
            neededdata.append(data[i]['{}. Categories'.format(i + 1)]['income_from_savings'])
        return neededdata
