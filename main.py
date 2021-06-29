import helper
import visualization as vs

paths = [
    '/SortedNumbers/Januar2020.csv',
    '/SortedNumbers/Februar2020.csv',
    '/SortedNumbers/March2020.csv',
    '/SortedNumbers/April2020.csv',
    '/SortedNumbers/Mai2020.csv',
    '/SortedNumbers/Juni2020.csv',
    '/SortedNumbers/Juli2020.csv',
    '/SortedNumbers/August2020.csv',
    '/SortedNumbers/September2020.csv',
]

helperdata = helper.Helper(paths).createLogicObjects()
vs.Vision(helperdata).year_basic_chart()
vs.Vision(helperdata).year_shisha_chart()



