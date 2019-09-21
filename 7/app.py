from flask import Flask, render_template, request, url_for, redirect
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST']		= 'localhost'
app.config['MYSQL_DATABASE_USER']		= 'root'
app.config['MYSQL_DATABASE_PASSWORD']	= ''
app.config['MYSQL_DATABASE_DB']			= 'simpleblog'
mysql.init_app(app)

@app.route('/<id>')
def post(id):
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM `posts` WHERE id = %s;",(id))
	data = cursor.fetchall()
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM `comments` WHERE `postId` = %s;",(id))
	comment = cursor.fetchall()
	print(comment)
	return render_template('post.html',data=data[0],comment=comment)

@app.route('/comment',methods=['POST'])
def comment():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO `comments` (`comment`,`postId`) VALUES (%s,%s)",(request.form['comment'],request.args['id']))
	conn.commit()
	conn.close()
	return redirect(f'/{request.args["id"]}')

@app.route('/')
def index():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM posts")
	data = cursor.fetchall()
	dataList = []
	if data is not None:
		for item in data:
			dataTemp = {
				'id':item[0],
				'title':item[1],
				'content':item[2],
				'createdBy':item[3]
			}
			dataList.append(dataTemp)
	return render_template('index.html', datalist=dataList)

@app.route('/add', methods=['GET','POST'])
def add():
	if request.method == "POST":
		#untuk execute ke tabel posts
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(f"""INSERT INTO `posts`(`title`, `content`, `createdBy`)
							VALUES (%s,%s,%s)""",(request.form['title'],request.form['article'],request.form['username']))
		conn.commit()
		conn.close()
		#untuk execute ke tabel user
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(f"""INSERT INTO `users`(`username`)
							VALUES (%s)""",(request.form['username']))
		conn.commit()
		conn.close()
		return url_for(index)
	else:
		return render_template('add.html')


if __name__ == '__main__':
	app.run(port=5000,debug=True)