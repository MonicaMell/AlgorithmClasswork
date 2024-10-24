class CustomDict:
    def  __init__(self):
        self.keys = []
        self.values = []

    def __setitem__(self, key, value):
        # This custom dictionary forces the key value pair to be string and lower
        key = str(key).lower()
        value = str(value).lower()

        if key in self.keys:
            i = self.keys.index(key)
            self.values[i] = value
            print("Key value pair updated")
        else:
            self.keys.append(key)
            self.values.append(value)
            print("Key value pair added")

    def __getitem__(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            raise KeyError("Key is not found")

    def __delitem__(self, key):
        if key in self.keys:
            i = self.keys.index(key)
            self.keys.pop(i)
            self.values.pop(i)
            print("Key Deleted")
        else:
            raise KeyError("Key is not found")

    def __contains__(self, key):
        # This custom dictionnary checks if the key exists, append "Key Exists" to its value
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] += " Key Exists"
            print("Key exists, this is shown in value name")

        return key in self.keys

    def __len__(self):
        return len(self.keys)

    # This custom dictionary also has a function to print it appropriately

    def __repr__(self):
        return "{" + ", ".join(f"{k}: {v}" for k, v in zip(self.keys, self.values)) + "}"
        # The output will be for exemple {name: Monica}, {age: 18}


my_dict = CustomDict()

my_dict["name"] = "Monica"
my_dict["age"] = 18

name = my_dict["name"]
print(name)

my_dict["age"] = 19

del my_dict["age"]

if "age" not in my_dict:
    print("Yes, it is Deleted")

print(len(my_dict))

print(my_dict)

