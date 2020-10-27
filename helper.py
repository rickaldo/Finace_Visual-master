import logic as lg


class Helper:
    def __init__(self, path):
        self.path = path

    def createLogicObjects(self):
        logic = []
        final = []
        for i in self.path:
            logic.append(lg.Logic(i))

        categories = self.createCategories(logic)
        subcategories = self.createSubCategories(logic)

        for i in range(len(logic)):
            final.append({
                '{}. Categories'.format(i+1): categories[i],
                '{}. SubCategories'.format(i+1): subcategories[i]
            })

        return final

    def createCategories(self, logic):
        categories = []
        for i in logic:
            categories.append(i.getCategories())

        return categories

    def createSubCategories(self, logic):
        categories = []
        for i in logic:
            categories.append(i.getSubCategories())

        return categories
