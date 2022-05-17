
def load(file):
    with open(file) as data:
        obj=data.read()
        data.close()

    obj = obj.split('\n')
    vertices=[]
    v2=[]
    indices=[]

    for i in obj:
        i2=i.split(" ")
        if i2[0] == "v":
            vertices.append(''.join(i[2:]))

        elif i2[0] == "f":
            for i3 in i2[1:]:
                indices.append(int(i3.split("/")[0])-1)

    for i in vertices:
        newi=i.split(" ")
        print(newi)
        v=[float(str(i2)) for i2 in newi]
        v2.append(v)

    return (v2,indices)

def process(vertices):
    result=[]
    for i in vertices:
        result.append(i+[0,0,-1,0,0]+[0.,0.5,1.])

    return result


