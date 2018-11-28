import mysql.connector
conn = mysql.connector.connect(
                            host="h2cwrn74535xdazj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com", # Host
                            user="y0z8umpce7iejqnf",
                            password="wig0tj0cp6sfv174",
                            database="ue1nsds7guapeehr"
)
cursor = conn.cursor()
sqlFormula = "INSERT INTO execList (userID, username, channel) VALUE ('a','b','c')"
cursor.execute(sqlFormula)
conn.commit()
cursor.close()
conn.close()
print("complete")