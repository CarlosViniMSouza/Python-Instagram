import instagram_explore as ie
import json

search = ie.user("CarlosViniMSouza")

datas = json.dumps(search, indent=4, sort_keys=True)

print(datas[15:400])

# don't working