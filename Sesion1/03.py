def funcion_1(df):
    genders = find_vals(df, 'Gender')
    filter_nan = remove_nan(df, 'ConvertedComp')

    count = 0
    for gen in genders:
        filter = (filter_nan) & (df['Gender'].str.contains(gen))
        print('\n\nResumen para '+gen+': ')
        print(df[filter]['ConvertedComp'].describe())
        df[filter].boxplot(column = 'ConvertedComp', sym='')
        plt.savefig(str(count))
        plt.clf()
        count = count + 1


def funcion_1(df):
    genders = find_vals(df, 'Gender')
    filter_nan = remove_nan(df, 'ConvertedComp')

    count = 0
    # for gen in genders:
    #     filter = (filter_nan) & (df['Gender'].str.contains(gen))
    #     print('\n\nResumen para '+gen+': ')
    #     print(df[filter]['ConvertedComp'].describe())
    #     df[filter].boxplot(column = 'ConvertedComp', sym='')
    #     plt.savefig(str(count))
    #     plt.clf()
    #     count = count + 1

#### Atajos ####
# ⌘ + /
# Ctrl + \
