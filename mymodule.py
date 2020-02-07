sorteddf = df.sort_values(by = ['company','body-style','price'], ascending = [True,True,False])

groupbycoy = sorteddf[['body-style','price']].groupby(sorteddf['company'])

# print(list(groupbycoy))

for company, grps in groupbycoy:
    print(company)
    print('----------')
    for i in grps.index:
        print(grps.value[i][0], end = ' ')
        print(grps.value[i][1])
# wefesfefes
