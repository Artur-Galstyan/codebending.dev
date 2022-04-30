from flask import Blueprint, render_template


blog_bp = Blueprint('blog_bp', __name__, template_folder='templates')


@blog_bp.route('/')
def home():
    return render_template('courses/index.html')


@blog_bp.route('/blog_post')
def blog_post():
    return render_template('courses/blog_post.html')
