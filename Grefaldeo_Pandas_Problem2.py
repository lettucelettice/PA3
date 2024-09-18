

import pandas as pd

cars = pd.read_csv{'cars.csv')
cars

#outputs the first five rows of the data frame with odd numbered columns
odd = cars.iloc[:5,::2]
odd

#output row for the model "Mazda RW4 Wag
cars.loc[[1]] 

#output cyl value for car model "Camaro Z28" 
cars.loc[[23],['cyl']] 

#output cyl and gear values for said car models
cars.loc[[1,18,28],['cyl','gear']] 

