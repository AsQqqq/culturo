



"""
  ______   ______ _____ _____ __  __ 
 / ___\ \ / / ___|_   _| ____|  \/  |
 \___ \\ V /\___ \ | | |  _| | |\/| |
  ___) || |  ___) || | | |___| |  | |
 |____/ |_| |____/ |_| |_____|_|  |_|

"""

from flask import render_template, send_file
from pages_backend import app
from flask_login import current_user


@app.route('/download_project')
def download_project():
    """Скачивание этого проекта"""
    try:
        print(current_user.username)
        if current_user.username == "download_project_uchitech":
                zip_path = "project/project.zip"
                return send_file(zip_path, as_attachment=True)
        else:
            return render_template('not_found.html'), 404
    except Exception as e:
        print(e)
        return render_template('not_found.html'), 404
    

def upload_system():
    return True