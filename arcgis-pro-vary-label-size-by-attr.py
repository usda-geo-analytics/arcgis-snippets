# Build using Esri Living Atlas US States Generalized Boundaries layer

def FindLabel ([SQMI], [STATE_NAME]):
    xs = "<FNT size = '10'>"
    sm = "<FNT size = '14'>"
    md = "<FNT size = '18'>"
    lg = "<FNT size = '22'>"
    xl = "<FNT size = '26'>"
    
    s = [SQMI]
    n = [STATE_NAME]
    
    if s < 1000:
        return xs + n + "</FNT>"
    elif s < 10000:
        return sm + n + "</FNT>"
    elif s < 100000:
        return md + n + "</FNT>"
    elif s < 200000:
        return lg + n + "</FNT>"
    else:
        return xl + n + "</FNT>"
