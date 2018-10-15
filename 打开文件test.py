import xlrd
file = xlrd.open_workbook(r'C:\Users\fariyland\Desktop\2017input.xlsx')  
tables = file.sheets() 
table = file.sheets()[0] #获取第一个sheet#
rows = table.nrows       #行数 
cols = table.ncols       #列数  
# print(rows)
tds=[]
i=1
while i<= rows-1:
    row = table.row_values(i) #获取第i行数据#
    col = table.col_values(0)#获取第1列数据#
    value = table.row_values(i)[0]    #获取第i行，第二列的数据#
    cell = table.cell(i, 0)       #读取第i行，第2列的单元格，这个方法获取的是单元格，并不是单元格中的值  
    cell_value = table.cell(i, 0).value  #单元格中的值  
    tds.append(cell_value)
    i+=1
print(int(tds))
