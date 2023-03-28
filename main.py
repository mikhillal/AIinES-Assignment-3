from flask import Flask, jsonify,request
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash


@app.route('/student/create', methods=['POST'])

#1. for creating a student data

def create_student():
    try:        
        _json = request.json
        _student_id = _json['student_id']
        _first_name = _json['first_name']
        _last_name = _json['last_name']
        _dob = _json['dob']	
        _due = _json['due']	
        if _student_id and  _first_name and _last_name and _dob and _due and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO student_info(student_id, first_name, last_name,dob, due) VALUES(%s, %s, %s, %s,%s)"
            bindData = (_student_id, _first_name ,  _last_name, _dob,_due)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('student added successfully!')
            respone.status_code = 200
            return respone
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()          
     
'''
StudentDB=[
    {'id':'1001',
     'first_name':'John',
     'last_name':'Paul',
     'DOB': '10/06/1997',
     'Due': '1600'
     },
     {'id':'1002',
     'first_name':'Rose',
     'last_name':'Mary',
     'DOB': '11/14/1995',
     'Due': '1000'
     },
]

@app.route('/student/getstudents', methods=['GET'])

def getStudents():
    return jsonify({"stud":StudentDB})

@app.route('/student/getstudent/<id>', methods=['GET'])

def filterstud(id):
    student=[stud for stud in StudentDB if(stud['id']==id)]
    print(student)
    return jsonify({"stud":student})



#2. for updating student details

@app.route('/student/updatestudent/<id>', methods=['PUT'])


def updatestudent(id):
    student=[stud for stud in StudentDB if(stud['id']==id)]
    if ('id' in request.json):
        print("Student available")

    if 'first_name' in request.json:
        student[0]['first_name']=request.json['first_name']
        
    return jsonify({"stud": student[0]})



#3. For Deleting a student data

@app.route('/student/removestudent/<id>', methods=['DELETE'])

def removestudent(id):
    student=[stud for stud in StudentDB if(stud['id']==id)]

    if(len(student)>0) :
        StudentDB.remove(student[0])
    return jsonify({"stud": student[0]})'''

if __name__=='__main__':
    app.run()

    