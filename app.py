"""
The main app for 
"""

from flask import Flask, request, render_template, redirect, jsonify


def get_nearest_stop(name):
    pass

app = Flask(__name__)

@app.route("/")
def get_route_input():

    #TODO: Populate bus lines from dictionary
    bus_lines=['171','172']

    try:
        bus_info = {
            'bus_line': request.form.get['bus_line'],
            'user_address': request.form.get['user_address'],
            'use_location': request.form.get['use_location'],
            'find_nearest_stop': request.form.get['find_nearest_stop']
        }

        return redirect("/nearest_stop", bus_info=bus_info)
    
    except:
        redirect(request.url)

    return render_template(
        "route_input.html", bus_lines=bus_lines
    )

@app.route("/nearest_stop", methods=['POST'])
def get_nearest_stop():

    try:
        bus_line=request.form.get('bus_line')
        user_address=request.form.get('user_address')
        use_location=request.form.get('use_location')
        find_nearest_stop=request.form.get('find_nearest_stop')
    
    #TODO: Populate list of stops for a line
        ## Make an api call for the line
        ## 
    #TODO: OR, given 'find_nearest_stop' == TRUE -- automatically select nearest stop
    #
    
    except Exception as error:
        return jsonify({
                'code': 400,
                'status': 'error',
                'message': f'an exception occurred: f{error}'
            }
        )
    
    return jsonify({
        'bus_line': bus_line,
        'user_address': user_address,
        'use_location': use_location,
        'find_nearest_stop': find_nearest_stop
    })

    #TODO: Call functions

@app.route("/stop_<stop_id>")
def get_stop_time():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)