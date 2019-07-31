import cx_Oracle

conn_str = 'sky/123456@127.0.0.1'
conn = cx_Oracle.connect(conn_str)
c = conn.cursor()
c.execute('select * from softwaredesc')
print "Employee No\tEmployee Name\n"
for column_1, column_2 in c.fetchall():
        print column_1, "\t\t", column_2
conn.close()
          
         

          



    
    
