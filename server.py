from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Please try again'



'''
@app.route('/index.html')
def my_home1():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/work1.html')
def work1():
    return render_template('work1.html')

@app.route('/work2.html')
def work2():
    return render_template('work2.html')

@app.route('/work3.html')
def work3():
    return render_template('work3.html')

@app.route('/work4.html')
def work4():
    return render_template('work4.html')

@app.route('/work5.html')
def work5():
    return render_template('work5.html')

@app.route('/work6.html')
def work6():
    return render_template('work6.html')

'''