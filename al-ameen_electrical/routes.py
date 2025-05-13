from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/services')
def services():
    return render_template('services.html')

@main_bp.route('/gallery')
def gallery():
    return render_template('gallery.html')

@main_bp.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@main_bp.route('/faq')
def faq():
    return render_template('faq.html')

@main_bp.route('/blog')
def blog():
    return render_template('blog.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Add logic to send an email or store the message
        return render_template('success.html')
    return render_template('contact.html')