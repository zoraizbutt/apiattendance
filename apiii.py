from flask import Flask, jsonify,json,request
import pyodbc
#from flask import Flask
from flask import jsonify, request, Response
app = Flask(__name__)

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-7DL0DAA\SQLEXPRESS;"
    "Database=attendancedb;"
    "UID=zoraiz;"
    "PWD=123456;"
    "Trusted_Connection=yes;"
)





@app.route('/AllStudent', methods=['GET','POST'])
def getAllStudent():
    cursor = conn.cursor()
    l={}
    cursor.execute("select * from teacher")
    rows = cursor.fetchall()
    #for row in cursor:
    l['Reg']=rows[0][0]
    l['First Name']=rows[0][1]



    return jsonify(l)

# @app.route('/api/users', methods=['GET'])
# def api_user():
#     cur = mysql.connection.cursor()
#     cur.execute("select * from users")
#     rv = cur.fetchall()
#     list_of_users = []
#     for row in rv:
#         data = {}
#         data['ID'] = row[0]
#         data['Name'] = row[1]
#         data['Age'] = row[2]
#         data['City'] = row[3]
#         list_of_users.append(data)
#     cur.close()
#     return jsonify(list_of_users)



if __name__ == '__main__':
    app.run(debug=True)
