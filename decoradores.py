from functools import wraps
from flask import session, redirect, url_for, flash


def login_requerido(f):
    @wraps(f)
    def decorada(*args, **kwargs):
        if 'user' not in session:
            flash("por favor inicia sesion","error")
            return redirect(url_for('login'))
        else:
            return f(*args, **kwargs)
    return decorada