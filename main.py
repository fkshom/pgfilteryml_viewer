from lib.aclmgr import AccessListManager
from flask import Flask, render_template, jsonify
from flask_cors import CORS

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

app = CustomFlask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1/rules')
def rules():
    return jsonify([
        dict(no=1, description="desc", source_ip="0.0.0.0"),
        dict(no=2, description="desc", source_ip="0.0.0.1"),
    ])

@app.route('/api/v1/hosts')
def hosts():
    return jsonify({
        'from': [1,2,3],
        'to': [4,5,6]
    }
        
    )

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

## おまじない
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)