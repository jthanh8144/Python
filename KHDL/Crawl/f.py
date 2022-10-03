

def handleAddress(s: str):
    result = ""
    if s.find(',') > 1:
        try:
            arr = s.split(',')
            for item in arr:
                if item.find('Phường') != -1 or item.find('Xã') != -1:
                    result += item.lstrip().rstrip() + ", "
            return result + arr[-2]
        except:
            return result
    else:
        return result
print(handleAddress(s))