import pandas as pd

#states = ["Vitoria", "Sao Paulo", "Rio de Janeiro"]
#population = [300000, 12000000, 8000000]

#dict_status = {"States":states, "Population":population}

#df_states = pd.DataFrame.from_dict(dict_status)

#df_states.to_csv("states.csv", index=False)

#for state in states:
#    if state == "Sao Paulo":
#        variable = state

# built in library
#with open("teste.txt", "w") as file:
#    file.write(variable)

#Handling exception errors: Try-except
new_list = [2,4,6, "Vitoria"]
for element in new_list:
    try:
        print(element/2)
    except:
        print("The element is not a number")