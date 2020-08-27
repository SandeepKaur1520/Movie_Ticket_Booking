import sqlite3
from sqlite3 import Error
import  os
import requests
import datetime
current_dir = os.getcwd()
db_location = current_dir + "\sqllite.db"
print(db_location)


def create_connection(db_file=db_location):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)



def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def init():
    conn = create_connection()

    qry = open('movie.sql', 'r').read()
    c = conn.cursor()
    sqlite3.complete_statement(qry)
    cursor = conn.cursor()
    try:
        cursor.executescript(qry)
        cursor.close()

        conn.close()
        
    except Exception as e:
        print(e)
        cursor.close()

        conn.close()

        raise



def auth_user(email,password):
    try:
        qry = "SELECT * FROM 'users' WHERE (username == '{}' OR email == '{}') AND  password == '{}';".format(email,email,password)
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(qry)
        rows = cur.fetchall()
        
        if len(rows)==1:
            print("User Exists")
            userdetails = {
                "UID":list(rows[0])[0],
                "username":list(rows[0])[1],
                "password":list(rows[0])[2],
                "email":list(rows[0])[3],
                "privilege":list(rows[0])[4]
            }
            return ["success",userdetails]
        if len(rows) == 0:
            print("user does not exits")
            return None
    except :
        return None
    

def getAllMovie():
    try:
        qry = "SELECT * FROM 'movies'"
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(qry)
        rows = cur.fetchall()
        
        if len(rows) > 0:
            return rows

        if len(rows) == 0:
            print("movies does not exits")
            return None
    except :
        return None

def getAllScreens():
    try:
        qry = "SELECT * FROM 'auditorium'"
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(qry)
        rows = cur.fetchall()
        
        if len(rows) > 0:
            return rows

        if len(rows) == 0:
            print("movies does not exits")
            return None
    except :
        return None

def get_image(image_path):
    try:
        # url = f'http://image.tmdb.org/t/p/original/{poster_path}'
        url = f'http://image.tmdb.org/t/p/w500/{image_path}'
        r = requests.get(url, allow_redirects=True)

        if r.status_code == 200:
             return r.content
        else:
            blob = convertToBinaryData("poster_placeholder_light.png")
            return blob
    except :
        blob = convertToBinaryData("poster_placeholder_light.png")
        return blob

def addMoie(movie=None):
    if movie == None:
        return None
    else:
        try:
            title = movie["title"]
            overview = movie['overview']
            adult = movie['adult']
            status = movie['status']
            release_date = movie['release_date']
            imdb_id = movie['imdb_id']
            tmdb_id = movie['id']
            tagline = movie['tagline']
            

            poster_path = movie['poster_path']
            backdrop_path = movie['backdrop_path']
            backdropBlob = convertToBinaryData("poster_placeholder_light.png")
            posterBlob = convertToBinaryData("poster_placeholder_light.png")
            if poster_path is not None:
                posterBlob = get_image(poster_path)
                print("Downloaded Image Data:" , type(posterBlob))

            if backdrop_path is not None:       
                backdropBlob =  get_image(backdrop_path)
                print("Downloaded Image Data:" , type(backdropBlob))

            qry = ''' INSERT INTO movies(title,overview,adult,status,release_date,imdb_id,tmdb_id,backdrop,poster,tagline)
                VALUES(?,?,?,?,?,?,?,?,?,?) '''

            data = (title,overview,adult,status,release_date,imdb_id,tmdb_id,backdropBlob,posterBlob,tagline)

            conn = create_connection()
            cur = conn.cursor()
            cur.execute(qry,data)
            conn.commit()
            cur.close()
            conn.close()
            return [0,"Data added Success Full"]
        except sqlite3.IntegrityError as err:
            print(err)
            return [1,err]

def addScreentoDb(screen=None):
    if screen == None:
        return None
    else:
        try:
            total_capcity = screen['total_seats']
            regular_seats= screen['regular_seats']
            regular_price= screen['regular_price']
            preminum_seats= screen['preminum_seats']
            preminum_prices= screen['preminum_prices']
            gold_seats= screen['gold_seats']
            gold_price= screen['gold_price']
            layout =screen['layout']

            qry = ''' INSERT INTO auditorium(total_seats,regular_seats,regular_price,preminum_seats,preminum_price,gold_seats,gold_price,layout)
                VALUES(?,?,?,?,?,?,?,?) '''

            data = (total_capcity,regular_seats,regular_price,preminum_seats,preminum_prices,gold_seats,gold_price,layout)
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(qry,data)
            conn.commit()
            cur.close()
            conn.close()
            return [0,"Data added Successfully"]
        except sqlite3.IntegrityError as err:
            print(err)
            return [1,err] # array[0] == 0 means succesfull array[0] == 1 means there is an error

            

def AddNewEmployeeToDB(username=None,password=None,email=None):
    try:
        if ( (username is not None) and (password is not None) and (email is not None) ):
            privilege = 'employee'
            qry = '''  INSERT INTO users(username,password,email,privilege) VALUES(?,?,?,?)'''

            data = (username,password,email,privilege)

            conn = create_connection()
            cur = conn.cursor()
            cur.execute(qry,data)
            conn.commit()
            cur.close()
            conn.close()
            return [0,"User Created Successfully"]
        else:
            return [1,f"Null Values not Allowed username={username}  password={password} email={email}"]

        
    except sqlite3.IntegrityError as err:
        return [1,err] # array[0] == 0 means succesfull array[0] == 1 means there is an error


def AddNewProjectionToDB(movie_ID=None,auditorium_ID=None,startTime=None,endTime=None,available_seats=None,total_seats=None):
    try:
        if ( (movie_ID is not None) and (auditorium_ID is not None) and (startTime is not None) and (endTime is not None) and (available_seats is not None) and (total_seats is not None)):
            
            qry = '''  INSERT INTO projections(movie_ID,auditorium_ID,startTime,endTime,available_seats,total_seats) VALUES(?,?,?,?,?,?)'''

            data = (movie_ID,auditorium_ID,startTime,endTime,available_seats,total_seats)

            conn = create_connection()
            cur = conn.cursor()
            cur.execute(qry,data)
            conn.commit()
            cur.close()
            conn.close()
            return [0,"Data Added Successfully"]
        else:
            return [1,f"Null Values not Allowed "]

        
    except sqlite3.IntegrityError as err:
        return [1,err] # array[0] == 0 means succesfull array[0] == 1 means there is an error    

def getProjections(datetime_str=None):# datetime_str == 'YYYY-MM-DD HH:MM:SS'
    try:
        if datetime_str is None:
            qry = "SELECT * FROM 'projections'"
        
        if datetime_str is not None:
            try:
                datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                qry = f"SELECT * FROM 'projections' WHERE startTime > '{datetime_str}'"
            except ValueError:
                return None
            

        conn = create_connection()
        cur = conn.cursor()
        cur.execute(qry)
        rows = cur.fetchall()
        
        if len(rows) > 0:
            return rows

        if len(rows) == 0:
            print("movies does not exits")
            return None
    except :
        return None

def getMovieDetails(ID=None):
    try:
        if ID is None:
            return None
        
        if ID is not None:
           
            qry = f"SELECT * FROM 'movies' WHERE movie_ID = '{ID}'"
            
            

        conn = create_connection()
        cur = conn.cursor()
        cur.execute(qry)
        rows = cur.fetchall()
        
        if len(rows) > 0:
            return rows

        if len(rows) == 0:
            print("movies does not exits")
            return None
    except :
        return None
def getAuditoriumDetails(ID=None):
    try:
        if ID is None:
            return None
        
        if ID is not None:
           
            qry = f"SELECT * FROM 'auditorium' WHERE auditorium_ID = '{ID}'"
            
            

        conn = create_connection()
        cur = conn.cursor()
        cur.execute(qry)
        rows = cur.fetchall()
        
        if len(rows) > 0:
            return rows

        if len(rows) == 0:
            print("movies does not exits")
            return None
    except :
        return None


if not os.path.exists(db_location):
    print("creating db")
    init()
else:
    print("db already exits")

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData