mark = {"Kaustubh" : 34,
    "Saswata": 24,
        "Tanudip" : 37,
            "Aritra" : 31    }

print(mark)
print(mark.items())
print(mark.keys())
print(mark.values())
mark.update({"Kaustubh":38 , "Arindam":16})
print(mark)

print(mark.get("Kaustubh"))
print(mark.pop("Aritra"))
print(mark)
