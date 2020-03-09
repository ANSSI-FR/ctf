# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, render_template_string, abort, Response
from wtforms import Form, StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import input_required, optional
from functools import wraps
from json import load as json_load

with open("content.json", encoding='utf-8') as f:
    POSTS = json_load(f)["posts"]

app = Flask(__name__)

def dangerous(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            debug_msg = ""
            # FIXME: tplmap still bypasses my test
            try:
                if "tplmap" in request.headers["User-Agent"].lower():
                    return render_template("error.html", error_code=403, 
                        error_message="Requête bloquée par le WAF"), 403
            except:
                pass
            for field, data in request.form.items():
                try:
                    tmp = render_template_string(data)
                except:
                    abort(500)
                # TODO
                if field == "comment":
                    debug_msg = tmp
                if len(data) != len(tmp):
                    r = Response(render_template("error.html", error_code=403, 
                        error_message="Requête bloquée par le WAF"), 403)
                    if len(data) > len(tmp):
                        r.headers["X-Waf-Debug"] = "BLOCKED; REASON: input longer than result"
                    else:
                        r.headers["X-Waf-Debug"] = "BLOCKED; REASON: input shorter than result"
                    return r
            # TODO: remove this
            r = Response(f(*args, **kwargs), 200)
            r.headers["X-Waf-Debug"] = "'%s' == '%s'" % (request.form["comment"], debug_msg)
            return r
        return f(*args, **kwargs)
    return decorated_function

class CommentForm(Form):
    nickname = StringField(u'Pseudonyme', validators=[input_required()])
    comment  = TextAreaField(u'Commentaire', validators=[optional()])
    preview = SubmitField("Previsualiser")
    post = SubmitField(u"Poster")

    def validate_post(self, field):
        if field.data is True:
            raise ValidationError("Comment section is not yet enabled!")

@app.errorhandler(500)
def server_error(e):
    return render_template("error.html", error_code=500, error_message="Erreur serveur"), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error_code=404, error_message="Page non trouvée"), 404

@app.route('/')
def homepage():
    return render_template("homepage.html", POSTS=POSTS)

@app.route('/post/<post_id>/', methods=["GET", "POST"])
@dangerous
def post(post_id=None):
    try:
        post_id = int(post_id)
    except TypeError:
        abort(404)
    if post_id < 1 or post_id > len(POSTS):
        abort(404)

    form=CommentForm(request.form)
    if request.method == "POST" and form.validate():
        return render_template("post.html", form=form, 
            POST=POSTS[post_id-1], post_id=post_id,
            preview_nick=form.nickname.data,
            preview_comment=form.comment.data)
    return render_template("post.html", form=form, POST=POSTS[post_id-1], post_id=post_id)    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
