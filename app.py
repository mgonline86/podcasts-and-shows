#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import sys
import json
import dateutil.parser
import babel
from flask import render_template, request, Response, flash, redirect, url_for, abort
from flask_moment import Moment
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask import Flask
from models import app, db, Show
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

moment = Moment(app)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format)


app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#
with app.app_context():
    db.create_all()

# VIEW SHOWS


@app.route('/')
def index():
    return render_template('pages/home.html', data=Show.query.order_by(Show.id).all())

# ADD SHOW


@app.route('/show/create', methods=['GET'])
def create_show_form():
    form = ShowForm()
    return render_template('forms/new_show.html', form=form, data=Show.query.order_by(Show.id).all())


@app.route('/show/create', methods=['POST'])
def create_show_submission():
    error = False
    try:
        show_name = request.form.get('show_name')
        host_name = request.form.get('host_name')
        period = request.form.get('period')
        episodes = request.form.get('episodes')
        about = request.form.get('about')
        image_link = request.form.get('image_link')
        show = Show(show_name=show_name, host_name=host_name, period=period, episodes=episodes, about=about,
                    image_link=image_link)
        db.session.add(show)
        db.session.commit()
        flash('Show ' + request.form['show_name'] +
              ' was successfully listed!')
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Show could not be listed.')
        abort(500)
    else:
        return render_template('pages/home.html', data=Show.query.order_by(Show.id).all())

# VIEW SHOW


@app.route('/show/<int:show_id>')
def view_show(show_id):

    show = Show.query.filter(Show.id == show_id).first()
    return render_template('pages/view_show.html', show=show, data=Show.query.order_by(Show.id).all())

# DELETE SHOW


@app.route('/show/<show_id>', methods=['POST'])
def delete_show(show_id):
    error = False
    try:
        Show.query.filter_by(id=show_id).delete()
        db.session.commit()
        flash('Show was successfully deleted!')
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Show could not be deleted.')
        abort(500)
    else:
        return redirect(url_for('index'))

# EDIT SHOW


@app.route('/show/<int:show_id>/edit', methods=['GET'])
def edit_show(show_id):
    form = ShowForm()
    d_show = Show.query.filter_by(id=show_id).first()
    show = {
        "id": d_show.id,
        "show_name": d_show.show_name,
        "host_name": d_show.host_name,
        "period": d_show.period,
        "episodes": d_show.episodes,
        "about": d_show.about,
        "image_link": d_show.image_link
    }
    return render_template('forms/edit_show.html', form=form, show=show, data=Show.query.order_by(Show.id).all())


@app.route('/show/<int:show_id>/edit', methods=['POST'])
def edit_show_submission(show_id):
    error = False
    try:
        show = Show.query.filter_by(id=show_id).first()
        show.show_name = request.form.get('show_name')
        show.host_name = request.form.get('host_name')
        show.period = request.form.get('period')
        show.episodes = request.form.get('episodes')
        show.about = request.form.get('about')
        show.image_link = request.form.get('image_link')
        db.session.commit()
        flash('show ' + request.form['show_name'] +
              ' was successfully updated!')
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Show ' + show.name + ' could not be updated.')
        abort(500)
    else:
        return redirect(url_for('view_show', show_id=show_id))


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#
# Default port:
if __name__ == '__main__':
    app.run(debug=True)
