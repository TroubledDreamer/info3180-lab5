# """
# Flask Documentation:     https://flask.palletsprojects.com/
# Jinja2 Documentation:    https://jinja.palletsprojects.com/
# Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
# This file creates your application.
# """
# import os
# from app import app, db
# from flask import render_template, request, jsonify, send_file, send_from_directory
# from app.forms import MovieForm
# from app.models import Movies
# from werkzeug.utils import secure_filename
# from flask_wtf.csrf import generate_csrf



# ###
# # Routing for your application.
# ###

# @app.route('/')
# def index():
#     return jsonify(message="This is the beginning of our API")


# ###
# # The functions below should be applicable to all Flask apps.
# ###

# # Here we define a function to collect form errors from Flask-WTF
# # which we can later use
# def form_errors(form):
#     error_messages = []
#     """Collects form errors"""
#     for field, errors in form.errors.items():
#         for error in errors:
#             message = u"Error in the %s field - %s" % (
#                     getattr(form, field).label.text,
#                     error
#                 )
#             error_messages.append(message)

#     return error_messages

# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)


# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also tell the browser not to cache the rendered page. If we wanted
#     to we could change max-age to 600 seconds which would be 10 minutes.
#     """
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=0'
#     return response


# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404


# @app.route('/api/v1/movies', methods=['GET'])
# def addMovie():
#     movies = Movies.query.all()
#     movieLst = []

#     for movie in movies:
#         movieLst.append({
#             "id": movie.id,
#             "title": movie.title,
#             "description": movie.description,
#             "poster": "/api/v1/posters/{}".format(movie.poster)
#         })
     
#     data = {
#         "movies": movieLst
#     }

#     return jsonify(data)

# @app.route('/api/v1/posters/<filename>')
# def getPoster(filename):
#     root_dir = os.getcwd()
#     return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

# @app.route('/api/v1/movies', methods=['POST'])
# def create_movie():
#     form = MovieForm()


#     if form.validate_on_submit():
#         title = form.title.data
#         poster = form.poster.data
#         description = form.description.data


#         movie = Movies(title, poster, description)
#         db.session.add(movie)
#         db.session.commit()


#         fileName = secure_filename(poster.filename)
#         poster.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))


#         return jsonify({
#             "message": "Movie Successfully added",
#             "title": title,
#             "poster": fileName,
#             "description": description
#         })
#     else:
#         return jsonify({
#             "errors": form_errors(form)
#         })


# @app.route('/api/v1/csrf-token', methods=['GET'])
# def get_csrf():
#     return jsonify({'csrf_token': generate_csrf()}) 







    
    


"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, jsonify, send_file, send_from_directory
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf

from app.models import Movies
from app.forms import MovieForm



###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
 return jsonify({'csrf_token': generate_csrf()}) 

@app.route('/api/v1/movies', methods=['GET'])
def addMovie():
    movies = Movies.query.all()
    movieLst = []

    for movie in movies:
        movieLst.append({
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "poster": "/api/v1/posters/{}".format(movie.poster)
        })
     
    data = {
        "movies": movieLst
    }

    return jsonify(data)

@app.route('/api/v1/posters/<filename>')
def getPoster(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)


@app.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            print(title)
            description = form.description.data
            poster = form.poster.data

            filename = secure_filename(poster.filename)
            poster.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename ))
            

            newMovie = Movies(title, description, filename)

            db.session.add(newMovie)
            db.session.commit()

           
            data = {
                    "message": "Movie Successfully added",
                    "title": title,
                    "description": description,
                    "poster": filename
                    }
            print(data)
            # print(jsonify(data))
            return jsonify(data)

        else:
            formErrors = form_errors(form)

            errors = {
                "errors" : formErrors
            }

            print(jsonify(errors))
            return jsonify(errors)

        






###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__  == "__main__":
    app.run()


















