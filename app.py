from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os
import datetime  
from site import USER_BASE, USER_SITE
import sqlite3
import json
current_date = datetime.date.today()
current_time = datetime.datetime.now().time()
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for


# Configure application
app = Flask(__name__)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///students.db")

@app.route("/")
def home(): 
    return render_template("byname1.html") 

@app.route("/byname1", methods=["GET", "POST"])
def byname1(): 
    if request.method == "POST":
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        input_data = request.form.get('input')
        data_array = input_data.split(',')
        data_array = [field.strip() for field in data_array]
        
        if len(data_array) == 5:
            name = data_array[0].strip()
            department = data_array[1].strip()
            major = data_array[2].strip()
            group_id = data_array[3].strip()
            number = data_array[4].strip()
        
            cursor.execute("SELECT department, major, group_id, number FROM students WHERE name = ?", (name,))
            result = cursor.fetchone()
                
            if result and str(result[0]).strip() == department and str(result[1]).strip() == major and str(result[2]).strip() == group_id and str(result[3]).strip() == number:
                return render_template("byname2.html", data_array_length=5, name=name, department=department, major=major, group_id=group_id, number=number)
                
            return render_template("byname2failure.html", name=name, department=department, major=major, group_id=group_id, number=number)

    
        elif len(data_array) == 4:

            first_data = data_array[0].strip()
            
            if first_data in ["computer science", "Sport"]:
                route_name = "chinageavant4"
                department = data_array[0].strip()
                major = data_array[1].strip()
                group_id = data_array[2].strip()
                number = data_array[3].strip()
                print(department,major,group_id,number)
                cursor.execute("SELECT name FROM students WHERE department = ? AND major = ? AND group_id = ? AND number = ?", (department, major, group_id, number))
                result = cursor.fetchone()
                name = str(result[0]).strip() 
                print(result)
                if result :
                    return render_template("byname2.html",route_name=route_name, data_array_length=4, name=name, department=department, major=major, group_id=group_id, number=number)
                else:
                    return render_template("byname2failure.html")
            else:
                route_name = "validation4"
                name = data_array[0].strip()
                department = data_array[1].strip()
                major = data_array[2].strip()
                group_id = data_array[3].strip()
                print(name,department,major,group_id)
                cursor.execute("SELECT department, major, group_id FROM students WHERE name = ?", (name,))
                result = cursor.fetchone()

                if result and str(result[0]).strip() == department and str(result[1]).strip() == major and str(result[2]).strip() == group_id:
                    print(name,str(result[0]).strip(),str(result[1]).strip(),str(result[2]).strip())
                    return render_template("byname2.html",route_name=route_name, data_array_length=4, name=name, department=department, major=major, group_id=group_id)
                else:
                    return render_template("byname2failure.html", name=name, department=department, major=major, group_id=group_id)    
                
        elif len(data_array) == 3:
            first_data = data_array[0].strip()
            
            if first_data in ["computer science", "Sport"]:
                route_name = "chinageavant3"
                department = data_array[0].strip()
                major = data_array[1].strip()
                group_id = data_array[2].strip()
                
                cursor.execute("SELECT name FROM students WHERE department = ? AND major = ? AND group_id = ?", (department, major, group_id))
                result = cursor.fetchall()
                
                if result:
                    names = [row[0] for row in result]
                    return render_template("byname2.html",route_name=route_name, data_array_length=3, names=names, department=department, major=major, group_id=group_id)
                else:
                    return render_template("byname2failure.html")
                
               
            else:
                route_name = "validation3"
                name = data_array[0].strip()
                department = data_array[1].strip()
                major = data_array[2].strip()
        
                
                cursor.execute("SELECT department, major FROM students WHERE name = ?", (name,))
                result = cursor.fetchone()
                
                if result and result[0] == department and result[1] == major  :
                    return render_template("byname2.html",route_name=route_name, data_array_length = 3, name=name, department=department, major=major)
                else:
                    return render_template("byname2failure.html", name=name, department=department, major=major)   
                
        elif len(data_array) == 2:
            first_data = data_array[0].strip()
            
            if first_data in ["computer science", "Sport"]:
                route_name = "chinageavant2"
                department = data_array[0].strip()
                major = data_array[1].strip()
                
                cursor.execute("SELECT name FROM students WHERE department = ? AND major = ?", (department, major))
                result = cursor.fetchall()
                
                if result:
                    names = [row[0] for row in result] 
                    return render_template("byname2.html",route_name=route_name, data_array_length=2, names=names, department=department, major=major)
                else:
                    return render_template("byname2failure.html")
            else :
                route_name = "validation2"
                name = data_array[0].strip()
                department = data_array[1].strip()
        
                cursor.execute("SELECT department FROM students WHERE name = ?", (name,))
                result = cursor.fetchone()
                
                if result and result[0] == department  :
                    return render_template("byname2.html",route_name=route_name, data_array_length = 2, name=name, department=department)
                else:
                    return render_template("byname2failure.html", name=name, department=department)          
                
            

        elif len(data_array) == 1:
            first_data = data_array[0].strip()
            
            if first_data in ["computer science", "Sport"]:
                route_name = "chinageavant1"
                department = data_array[0].strip()
                
                cursor.execute("SELECT name FROM students WHERE department = ?", (department,))
                result = cursor.fetchall()
                
                if result:
                    names = [row[0] for row in result]  # Extract names from the result
                    return render_template("byname2.html",route_name=route_name, data_array_length=1, names=names, department=department)
                else:
                    return render_template("byname2failure.html")
            else:    
                route_name = "chinagearriere1"
                name = data_array[0].strip()
                
                cursor.execute("SELECT department, major, group_id, number, image FROM students WHERE name = ?", (name,))
                result = cursor.fetchone()
                
                if result:
                    department = result[0]
                    major = result[1]
                    group_id = result[2]
                    number = result[3]
                    image = result[4]

                    return render_template("byname2.html",route_name=route_name, data_array_length= 1, name=name, department=department, major=major, group_id=group_id, number=number, image=image)
                    
                else:
                    return render_template("byname2failure.html", name=name)
    else:
        return render_template("byname1.html")
 
 
 
@app.route("/byname2", methods=["GET", "POST"])
def byname2(): 
    if request.method == "POST":
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        input_data = request.form.get('input')
        data_array = input_data.split(',')
        data_array = [field.strip() for field in data_array]
        
        if len(data_array) == 5:
            name = data_array[0].strip()
            department = data_array[1].strip()
            major = data_array[2].strip()
            group_id = data_array[3].strip()
            number = data_array[4].strip()
        
            cursor.execute("SELECT department, major, group_id, number FROM students WHERE name = ?", (name,))
            result = cursor.fetchone()
                
            if result and str(result[0]).strip() == department and str(result[1]).strip() == major and str(result[2]).strip() == group_id and str(result[3]).strip() == number:
                return render_template("byname2.html", data_array_length=5, name=name, department=department, major=major, group_id=group_id, number=number)
                
            return render_template("byname2failure.html", name=name, department=department, major=major, group_id=group_id, number=number)

    
        elif len(data_array) == 4:

            first_data = data_array[0].strip()
            
            if first_data in ["computer science", "Sport"]:
                route_name = "chinageavant4"
                department = data_array[0].strip()
                major = data_array[1].strip()
                group_id = data_array[2].strip()
                number = data_array[3].strip()
                print(department,major,group_id,number)
                cursor.execute("SELECT name FROM students WHERE department = ? AND major = ? AND group_id = ? AND number = ?", (department, major, group_id, number))
                result = cursor.fetchone()
                name = str(result[0]).strip() 
                print(result)
                if result :
                    return render_template("byname2.html",route_name=route_name, data_array_length=4, name=name, department=department, major=major, group_id=group_id, number=number)
                else:
                    return render_template("byname2failure.html")
            else:
                route_name = "validation4"
                name = data_array[0].strip()
                department = data_array[1].strip()
                major = data_array[2].strip()
                group_id = data_array[3].strip()
                print(name,department,major,group_id)
                cursor.execute("SELECT department, major, group_id FROM students WHERE name = ?", (name,))
                result = cursor.fetchone()

                if result and str(result[0]).strip() == department and str(result[1]).strip() == major and str(result[2]).strip() == group_id:
                    print(name,str(result[0]).strip(),str(result[1]).strip(),str(result[2]).strip())
                    return render_template("byname2.html",route_name=route_name, data_array_length=4, name=name, department=department, major=major, group_id=group_id)
                else:
                    return render_template("byname2failure.html", name=name, department=department, major=major, group_id=group_id)    
                
        elif len(data_array) == 3:
            first_data = data_array[0].strip()
            
            if first_data in ["computer science", "Sport"]:
                route_name = "chinageavant3"
                department = data_array[0].strip()
                major = data_array[1].strip()
                group_id = data_array[2].strip()
                
                cursor.execute("SELECT name FROM students WHERE department = ? AND major = ? AND group_id = ?", (department, major, group_id))
                result = cursor.fetchall()
                
                if result:
                    names = [row[0] for row in result]
                    return render_template("byname2.html",route_name=route_name, data_array_length=3, names=names, department=department, major=major, group_id=group_id)
                else:
                    return render_template("byname2failure.html")
                
               
            else:
                route_name = "validation3"
                name = data_array[0].strip()
                department = data_array[1].strip()
                major = data_array[2].strip()
        
                
                cursor.execute("SELECT department, major FROM students WHERE name = ?", (name,))
                result = cursor.fetchone()
                
                if result and result[0] == department and result[1] == major  :
                    return render_template("byname2.html",route_name=route_name, data_array_length = 3, name=name, department=department, major=major)
                else:
                    return render_template("byname2failure.html", name=name, department=department, major=major)   
                
        elif len(data_array) == 2:
            first_data = data_array[0].strip()
            
            if first_data in ["computer science", "Sport"]:
                route_name = "chinageavant2"
                department = data_array[0].strip()
                major = data_array[1].strip()
                
                cursor.execute("SELECT name FROM students WHERE department = ? AND major = ?", (department, major))
                result = cursor.fetchall()
                
                if result:
                    names = [row[0] for row in result] 
                    return render_template("byname2.html",route_name=route_name, data_array_length=2, names=names, department=department, major=major)
                else:
                    return render_template("byname2failure.html")
            else :
                route_name = "validation2"
                name = data_array[0].strip()
                department = data_array[1].strip()
        
                cursor.execute("SELECT department FROM students WHERE name = ?", (name,))
                result = cursor.fetchone()
                
                if result and result[0] == department  :
                    return render_template("byname2.html",route_name=route_name, data_array_length = 2, name=name, department=department)
                else:
                    return render_template("byname2failure.html", name=name, department=department)          
                
            

        elif len(data_array) == 1:
            first_data = data_array[0].strip()
            
            if first_data in ["computer science", "Sport"]:
                route_name = "chinageavant1"
                department = data_array[0].strip()
                
                cursor.execute("SELECT name FROM students WHERE department = ?", (department,))
                result = cursor.fetchall()
                
                if result:
                    names = [row[0] for row in result]  # Extract names from the result
                    return render_template("byname2.html",route_name=route_name, data_array_length=1, names=names, department=department)
                else:
                    return render_template("byname2failure.html")
            else:    
                route_name = "chinagearriere1"
                name = data_array[0].strip()
                
                cursor.execute("SELECT department, major, group_id, number, image FROM students WHERE name = ?", (name,))
                result = cursor.fetchone()
                
                if result:
                    department = result[0]
                    major = result[1]
                    group_id = result[2]
                    number = result[3]
                    image = result[4]

                    return render_template("byname2.html",route_name=route_name, data_array_length= 1, name=name, department=department, major=major, group_id=group_id, number=number, image=image)
                    
                else:
                    return render_template("byname2failure.html", name=name)
    else:
        return render_template("byname1.html")
 
    













   