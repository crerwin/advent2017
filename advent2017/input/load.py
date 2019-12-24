import os

def get_input(day):
    inputs = {
        1: "file",
        2: "file",
        3: 277678,
        4: "file",
        5: "file",
        6: "file"
    }
    if inputs[day] == "file":
        return load_from_file(day)
    else:
        return inputs[day]

def load_from_file(day):
        input_dir = os.path.dirname(__file__)
        filename = input_dir + "/day" + str(day) + ".txt"
        try:
            f = open(filename, 'r')
        except:
            print("can't open file")
        content = f.read()
        f.close()
        return content
