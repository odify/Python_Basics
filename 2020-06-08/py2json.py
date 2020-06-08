#JSON===CONVERTER

import json

x = {
  "name": "ferdi",
  "age": 28,
  "city": "l-town"
}


#Convert into JSON

y = json.dumps(x)

#JSON CREATED

print(y)