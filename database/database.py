import  mongoengine
from mongoengine import connect

def global_init():
    print("Connecting to mongo")
    connect("sample_airbnb",
            host="mongocluster0-afh90.gcp.mongodb.net",
            username="atlasAdmin",
            password="password666")
