def sumaacum(arr):
    result=0
    nuevlist=[]
    for i in range(len(arr)):
        result += arr[i]
        nuevlist.append(result)
    return nuevlist

def sumaacum2(arr):
    result=0
    for i in range(len(arr)):
        result += arr[i]
        arr[i] = result
    return arr

def elimina(arr):
    if len(arr) > 2:
        del arr[0]
        del arr[-1]
    else:
        print("Necesito un arreglo de más de 1 posición")
    return arr

def ordenada(arr):
    newarr = sorted(arr)
    if newarr == arr:
        print("Esta ordenada")
    else:
        print("No esta ordenada")

a=[1,2,3]
#print(sumaacum(a))
#print(sumaacum2(a))
#print(elimina(a))
ordenada(a)
