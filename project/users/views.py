from project import db, bcrypt
from flask import render_template, redirect, request, url_for, Blueprint, flash

users_blueprint = Blueprint(
    'users'
    __name__,
    template_folder = 'templates'
)
