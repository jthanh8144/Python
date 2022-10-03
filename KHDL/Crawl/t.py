def handlePrice(price: str, area: str):
    result = ''
    if price != 'Thỏa thuận':
        if price.find('m²') != -1:
            if price.find('triệu') == -1:
                result = str(float(price.split(' ')[0]) * float(area))
            else:
                result = str(float(price.split(' ')[0]) * float(area) * 1000)
        elif price.find('tỷ') != -1:
            result = str(float(price.split(' ')[0]) * 1000)
    return result

s1 = '45 tỷ'
s2 = '240'
print(handlePrice(s1, s2))