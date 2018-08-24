import json
print(dir(json))
people_string='''
{
    "person":
        [
            {
            "names":"Rohit",
            "mob":9308779568,
            "address":"chatra",
            "email":"rohit@gmail.com"
             },
            {
            "name":"Rahul",
             "mob":7631189703,
             "address":"Ramgarh",
             "email":"rahul@gmail.com"
             }
        ]
}'''

data=json.loads(people_string)
with open("newdemo.json",'r') as f :
    python_data=json.load(f)
    print(python_data["person"])





