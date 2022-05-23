from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


# ! ////// CREATE  //////
# TODO CREATE REQUIRES TWO ROUTES:
# TODO ONE TO DISPLAY THE FORM:
@app.route('/ninja/new')
def new_ninja():
    return render_template("new_ninja.html",dojos=Dojo.get_all())

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/ninja/create',methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(f"/dojo/show/{request.form['dojo_id']}")

# TODO READ ALL
@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html",ninjas=Ninja.get_all())

# TODO READ ONE
@app.route('/ninja/show/<int:id>')
def show_ninjas(id):
    data ={ 
        "id":id
    }
    return render_template("show_ninja.html",ninja=Ninja.get_one(data))

# ! ///// UPDATE /////
# TODO UPDATE REQUIRES TWO ROUTES
# TODO ONE TO SHOW THE FORM
@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    data ={ 
        "id":id
    }
    return render_template("edit_ninja.html",ninja=Ninja.get_one(data))

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/ninja/update',methods=['POST'])
def update_ninja():
    Ninja.update(request.form)
    return redirect('/ninjas')

# ! ///// DELETE //////
@app.route('/ninja/destroy/<int:id>')
def destroy_ninja(id):
    data ={
        'id': id
    }
    Ninja.destroy(data)
    return redirect('/ninjas')