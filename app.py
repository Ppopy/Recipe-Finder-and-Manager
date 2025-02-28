from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get the ingredients from the form
    ingredients = request.form['ingredients']
    ingredients_list = ingredients.split(',')  # Split ingredients into a list
    
    # Here you would add your logic to search for recipes based on the ingredients
    # For now, let's just return the ingredients that were entered
    return render_template('search_results.html', ingredients_list=ingredients_list)

if __name__ == '__main__':
    app.run(debug=True)
