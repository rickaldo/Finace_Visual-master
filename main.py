import helper
import visualization as vs

paths = [
    '/Users/ricked-corp/Documents/SortedNumbers/Januar2020.csv',
    '/Users/ricked-corp/Documents/SortedNumbers/Februar2020.csv',
    '/Users/ricked-corp/Documents/SortedNumbers/March2020.csv',
    '/Users/ricked-corp/Documents/SortedNumbers/April2020.csv',
    '/Users/ricked-corp/Documents/SortedNumbers/Mai2020.csv',
    '/Users/ricked-corp/Documents/SortedNumbers/Juni2020.csv',
    '/Users/ricked-corp/Documents/SortedNumbers/Juli2020.csv',
    '/Users/ricked-corp/Documents/SortedNumbers/August2020.csv',
    '/Users/ricked-corp/Documents/SortedNumbers/September2020.csv',
]

helperdata = helper.Helper(paths).createLogicObjects()
vs.Vision(helperdata).year_basic_chart()



