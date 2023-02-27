import numpy as np

def ch(df, hover_data):
    
    customdata = np.stack([df.index] + [df[hover_data[i]] for i in range(1, len(hover_data))], axis = -1)
    
    hovertemplate = "<br>".join(["<b>%{customdata[0]}</b>"] + ["<b>" + str(hover_data[i]) + ":</b> %{customdata[" + str(i) + "]}" for i in range(1, len(hover_data))])
    
    return customdata, hovertemplate