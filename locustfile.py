from locust import HttpLocust, TaskSet, task

def index(l):
    l.client.get("/")

def getFilms(l):
    l.client.get("/api/films/")       

def getPeople(l):
    l.client.get("/api/people")

def getPerson(l):
    l.client.get("/api/people/12")  

def getSpecies(l):
    l.client.get("/api/species/");  

def searchPerson(l):
    l.client.get("/api/people/?search=r2");  

def getStarships(l):
    l.client.get("/api/starships")

def getSchemaStarship(l):
    l.client.get("/api/starships/schema/"); 

def getPlanets(l):
    l.client.get("/api/planets")

def getPlanet(l):
    l.client.get("/api/planets/14/")

class UserBehavior(TaskSet):
    tasks = {
        index: 2, 
        getFilms: 1, 
        getPeople: 1, 
        getPerson: 1, 
        getSpecies: 1,
        searchPerson: 1, 
        getStarships : 1, 
        getPlanets: 1, 
        getPlanet: 1
    }

class MyLocust(HttpLocust):
    task_set = UserBehavior
    #each simulated user will wait between 5 and 15 seconds between the requests
    min_wait = 5000
    max_wait = 15000
