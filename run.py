from app import createapp

app=createapp()

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')