from flask import Flask, render_template
app = Flask(__name__,template_folder='template')
#in the function return render_template(‘index.html’)
@app.route("/first")
def first_webpage():
    name='Suchismita'
    # Pass the variable in the template
    return render_template('index.html', index_variable=name)
app.run(debug=True)



