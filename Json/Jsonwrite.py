data=[
    {"name":"arun","age":25},
    {"name":"amal","age":20},
    {"name":"yamal","age":19}
]
import json
f=open("xos.json","w")
json.dump(data,f)