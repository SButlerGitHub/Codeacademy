from flask import Flask
from helper import pets #testtest

app = Flask(__name__) 

@app.route('/')
def index(): 
  return '''<h1> Adopt a pet ! </h1> <p>Browse through the links below to find your new furry friend: </p>
  <ul> 
     <li><a href="/animals/dogs">Dogs</a>
     </li>
     <li><a href="/animals/cats">Cats</a>
     </li>
     <li><a href="/animals/rabbits">Rabbits</a>
     </li> 
  </ul>'''
#new animal route
@app.route('/animals/<pet_type>')
def animals(pet_type):
 html = f'<h1>List of {pet_type}</h1><ul>'
 for index, pet in enumerate(pets[pet_type]):
  html += f'<li><a href="/animal/{pet_type}/{index}">{pet["name"]}</a></li>'
  html += '</ul>'
  return html 

@app.route('/animal/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id): #access the list of pets
   pet_list = pets[pet_type] 
   pet = pet_list[pet_id] 
   html = f'''
   <h1>{pet["name"]}</h1>
   <img src="{pet["url"]}"
   alt="Photo of {pet["name"]}">
   <p>{pet["description"]}</p>
   </ul>
       <li>Breed:
    {pet["breed"]}</li>
         <li>Age: {pet["age"]}
    </li>
      </ul>'''


   return html
