"""
acronyms = {"LOL": "laugh out loud",
            "IDK": "I don't know",
            "TBH": "to be honest"}
print(acronyms["LOL"])


# Creating a dictionary and adding values
acronyms = {}
acronyms["LOL"] = "laugh out loud"
acronyms["IDK"] = "I don't know"
acronyms["TBH"] = "to be honest"
print(acronyms)

# Updating values in our dictionary
acronyms["TBH"] = "honestly"
print(acronyms["TBH"])

# To delete a value from a dictionary
del acronyms["LOL"]
print(acronyms["LOL"])


# Getting an item that's NOT in the dictionary
acronyms = {"LOL": "laugh out loud", "IDK": "I don't know"}
# Using get() won't crash your program with an error
definition = acronyms.get("BTW") 
# this line means that if there is an existing definition or key, then print
if definition:
    print(definition)
else:
    print("Key doesn't exist")
"""
# Using a Dictionary to Translate a Sentence
acronyms = {"LOL": "laugh out loud",
            "IDK": "I don't know",
            "TBH": "to be honest"}
sentence = "IDK" + " what happened " + "TBH"
translation = acronyms.get("IDK") + " what happened " + acronyms.get("TBH")
print("sentence:", sentence)
print("translation", translation)
