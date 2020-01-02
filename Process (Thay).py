import pyodbc

f = open("DATA_FILE - Copy.txt", mode= "r")

listSanPhamStr = []
sanPhamStr = ""

for line in f:
    if line == '{SAN_PHAM\n':
        continue

    if line == '}SAN_PHAM\n':
        listSanPhamStr.append(sanPhamStr)
        sanPhamStr = ""
        continue

    sanPhamStr += line

print(listSanPhamStr)

class Product:
    productID = ""
    productName = ""
    productPrice = ""
    productQty = 0

danhSachDoiTuong = []
for i in range(len(listSanPhamStr)):
    s = listSanPhamStr[i]
    listAttribute = s.split('\n')
    listAttribute = list(filter(None, listAttribute));

    sp = Product()
    for j in range(len(listAttribute)):
        productAttribute = listAttribute[j].split(':')
        if productAttribute[0] == "ID_SP":
           sp.productID = productAttribute[1]
        if productAttribute[0] == "TEN_SP":
            sp.productName = productAttribute[1]
        if productAttribute[0] == "GIA_SP":
            sp.productPrice = productAttribute[1]
        if productAttribute[0] == "SL_SP ":
            sp.productQty = productAttribute[1]

    danhSachDoiTuong.append(sp)

for s in danhSachDoiTuong:
    print(s.productID, "-", s.productName, "-", s.productPrice, "-", s.productQty)




conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DLAP-0064;'
                      'Database=QUAN_LY_NHAN_VIEN;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

for p in danhSachDoiTuong:
    s = "";
    ma = p.productID
    ten = p.productName
    gia = p.productPrice
    sl = p.productQty

    s = "INSERT INTO PRODUCT VALUES('" + ma + "','" + ten + "','" + gia + "'," + sl + ")"
    cursor.execute(s)

    conn.comit();
