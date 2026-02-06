# function mit integrierten variablen als parameter, die variablen liegen außerhalb der function
# da die variablen als paramter/argument übernommen wurde, erwartet die function mindestens genauso viel paramter
# beim functions aufruf
argument_var_name1 = "Jakob"
argument_var_Geburtsjahr1 = 1990, 10, 7

def function(argument_var_name1, argument_var_Geburtsjahr1):
    print("hallo ich heiße: ", argument_var_name1, "mein geburtsjahr ist: ", argument_var_Geburtsjahr1)

function(argument_var_name1, argument_var_Geburtsjahr1)
