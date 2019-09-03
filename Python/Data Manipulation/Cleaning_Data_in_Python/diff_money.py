from numpy import NaN
import pandas as pd

def diff_money(row, pattern):
    icost = row['Initial Cost']
    tef = row['Total Est. Fee']
    
    if bool(pattern.match(icost)) and bool(pattern.match(tef)):
        icost = icost.replace('$', '')
        tef = tef.replace('$', '')
        
        icost = float(icost)
        tef = float(tef)
        
        return icost - tef
    else:
        return(NaN)