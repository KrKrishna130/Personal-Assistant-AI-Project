# end point recieved krne ka kaam krnge ye files
from flask import Flask,render_template ,url_for,request,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    # yaha Query le rahe hai URL through
    name=request.args.get("name",default="selke")
    sub=request.args.get("sub",default="java")
    # http://127.0.0.1:5000/?name=krishna+kumar&sub=AI
    # http://127.0.0.1:5000/?&sub=AI thw default will work
    # i.e=your query was: selke & subject: AI
    print(name)
    print(sub) 

    data={
        "msg":"Welcome to the paltform"
      }
    # return render_template("index.html",name=name,sub=sub)
    return jsonify(data),200


# URL ==> end point '/login'  jb bhi ho to login page return kr dega
@app.route("/login",methods={"GET","POST"})
def login_page():
    if request.method=="POST":
       
        print(request.form)
        name=request.form["username"]
        password=request.form["password"]
        # here we need to send data in DB and then verify then login
        # return f"<p> welcome{name}!</p>"
        freinds=["Santosh","Yogesh","krishna","Dalchand"]
        header="<header>Welcome To Bihar </header>"

        return render_template("welcome.html",name=name,password=password,freinds=freinds,header=header)
    else:
    
     return render_template("login.html")





if __name__=="__main__":
    app.run(debug=True)
