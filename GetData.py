from DBConnection import DBConnection


class GetData:
    def main(file):
        f = open("ETFs/" + file + ".us.txt")
        lines = f.readlines()
        lsize = len(lines)
        lsize = lsize - 1

        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("delete from data")
        cursor.execute("delete from dataset")
        database.commit()

        for r in range(800):
            d = lines[lsize - r]
            d = d.split(",")
            query = "insert into data values(" + str(r) + ",'" + d[0] + "','" + d[1] + "','" + d[2] + "','" + d[
                3] + "','" + d[4] + "','" + d[5] + "','" + d[6].strip() + "')"
            #print(query)
            cursor.execute(query)
            database.commit()
            start = float(d[1])
            maxp = float(d[2])
            close = float(d[4])

            s_m = start - maxp
            s_c = start - close
            print(s_m, s_c)

            res = ''
            if start < close:
                res = 'profit'
            else:
                res = 'loss'

            try:
                d2 = lines[lsize - r + 1]
                d2 = d2.split(",")
                #print("---------------------", d2)
                #print(d[2])
                #print("...............", d2[2])
                #print(d[1], d2[1], type(d[1]), type(d2[1]))
                diff = (float(d[1]) - float(d2[1]))
                query = "insert into dataset values('"+str(diff) + "','" + str(s_m) + "','" + str(s_c) + "','" + res + "')"
                #print(query)
				#print(diff,s_m,s_c,res)
                cursor.execute(query)
                database.commit()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    GetData.main("aadr")
