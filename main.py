# Get -> a request is made
# post  -> some data is given to server by user
# put/patch -> update put-> full update patch-> partial update
# delete -> something is deleted

# end points -> after/wali chiz in link
# static -> media files
# template -> index.html

import pickle

from flask import Flask, render_template, request, jsonify

# oops
# Classes,objects,methods.inheritance,polymorphism, abstraction,encapsulation,decorators,generators,dundermethods,abstract method, static methods

# create an object of the class Flask

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

# url/
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predict',methods = ['GET', 'POST'])

def predict():
        prediction = model.predict([[request.form.get('mean_radius'),request.form.get('mean_texture'),request.form.get('mean_perimeter'),request.form.get('mean_area'),request.form.get('mean_smoothness'),request.form.get('mean_compactness'),request.form.get('mean_concavity'),request.form.get('mean_concave_points'),request.form.get('mean_symmetry'),request.form.get('mean_fractal_dimension'),request.form.get('radius_error'),request.form.get('texture_error'),request.form.get('perimeter_error'),request.form.get('area_error'),request.form.get('smoothness_error'),request.form.get('compactness_error'),request.form.get('concavity_error'),request.form.get('concave_points_error'),request.form.get('symmetry_error'),request.form.get('fractal_dimension_error'),request.form.get('worst_radius'),request.form.get('worst_texture'),request.form.get('worst_perimeter'),request.form.get('worst_area'),request.form.get('worst_smoothness'),request.form.get('worst_compactness'),request.form.get('worst_concavity'),request.form.get('worst_concave_points'),request.form.get('worst_symmetry'),request.form.get('worst_fractal_dimension'),]])
#         prediction = model.predict([[12.45, 15.32, 82.56, 550.1, 0.095, 0.065, 0.043, 0.023, 0.168, 0.056, 
# 0.3, 0.8, 1.2, 12.34, 0.005, 0.008, 0.006, 0.004, 0.012, 0.001, 
# 14.32, 19.12, 93.48, 710.8, 0.135, 0.084, 0.065, 0.037, 0.202, 0.063]])
        output = prediction[0]
    
        print(f"predicted value : {output}")
        ans = "Negative"
        if(output):
            ans = "Positive"
        else:
            ans = "Negative"
        return render_template('index2.html',prediction_text = f'Cancer report : {ans}')


    

if __name__ == '__main__':
    app.run(debug = True)

