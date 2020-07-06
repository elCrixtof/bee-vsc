""" FRAGMENTO DE CODIGO PARA EQUIS COSA """
def funcion_2(df):
    ethnicities = find_vals(df, 'Ethnicity')
    filter_nan = remove_nan(df, 'ConvertedComp')

    count = 0
    for ethnicity in ethnicities:
        filter = (filter_nan) & (df['Ethnicity'].str.contains(ethnicity))
        print('\n\nResumen para '+ethnicity+': ')
        print(df[filter]['ConvertedComp'].describe())
        df[filter].boxplot(column = 'ConvertedComp')
        plt.savefig(str(count))
        plt.clf()
        count = count + 1

def funcion_2(df):
    ethnicities = find_vals(df, 'Ethnicity')
    filter_nan = remove_nan(df, 'ConvertedComp')

    """ count = 0
    for ethnicity in ethnicities:
        filter = (filter_nan) & (df['Ethnicity'].str.contains(ethnicity))
        print('\n\nResumen para '+ethnicity+': ')
        print(df[filter]['ConvertedComp'].describe())
        df[filter].boxplot(column = 'ConvertedComp')
        plt.savefig(str(count))
        plt.clf()
        count = count + 1 """

#### Atajos ####
# ⌘ /
# ⇧ ⌥ A

# Ctrl + \
# Shift + Alt + A