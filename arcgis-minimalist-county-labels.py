# Sometimes you JUST WANT THE COUNTY NAME...not "county" after the county name, or "borough" or "census area" or whatever.
# This label expression (python) filters out all the crap you don't necessarily have space for,
# accounts for Washington DC, Census Area, Bureau, City and Bureau...pretty much everything I could find.
# You just get the name, not the type of county.
# For use with Esri Living Atlas' "US Counties Generalized" or similar/derivative datasets

def FindLabel ( [NAME] ):
    nam = [NAME]    
    if " city" in nam:
        nam = nam.replace(" city", " City")
    if nam == "District of Columbia":
        label = nam
    elif "Census Area" in nam:
        label = nam.rsplit(" ", 2)[0]
    elif "City and Borough" in nam:
        label = nam.rsplit(" ", 3)[0]
    else:
        label = nam.rsplit(" ", 1)[0]
    return label
