import json
student = {
    "Name": "Farhan",
    "Age": 20
}
with open('student.json','w') as file:
  json.dump(student,file,indent=4)
with open('student.json','r') as file:
   print(json.load(file))
  

  