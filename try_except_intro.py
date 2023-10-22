acronyms = {"LOL": "laugh out loud",
            "IDK": "I don't know",
            "TBH": "to be honest"}
try:
    definition = acronyms["BTW"] # <--- Code that might cause an exception
    print(definition)
except:
    print("The key does not exist") # <--- Print an error message. When the program runs, the error message will print and now the program can keep running.
finally: 
    print("The acronyms we have defined are:")
    for acronym in acronyms:
        print(acronym)
print("The program keeps going...")
