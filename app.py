from flask import Flask, render_template, Response
from data import csv_to_pandas, get_plot_filenames


app = Flask(__name__)
# load data
graduates_df = csv_to_pandas(file_name='grade_stats_auswertung.csv', delimiter=';')
plot_files_dict = get_plot_filenames()


@app.route('/')
def web_index():
    return render_template('home.html')


@app.route('/table')
def table():
    return render_template("table.html", data=graduates_df)


@app.route('/plots')
def plots():
    return render_template('plots.html')


@app.route('/plots/<string:plot_type>/<string:degree>')
def plot_list(degree, plot_type):
    return render_template(f'{plot_type}.html', degree=degree, images=plot_files_dict[degree][plot_type])


@app.route('/downloads/<string:file_name>')
def download(file_name):
    with open(f'downloads/{file_name}', 'r') as file:
        return_file = file.read().encode('utf8')

    return Response(return_file,
                    mimetype="text/csv",
                    headers={"Content-disposition": f"attachment; filename={file_name}"})


if __name__ == '__main__':
    app.run(debug=True)
