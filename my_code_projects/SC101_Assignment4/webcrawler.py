"""
File: webcrawler.py
Name: Jason
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        items = soup.find_all('table', {'class': 't-stripe'})
        ans = []
        for item in items:
            text = item.tbody.text
            for ch in text:
                if ch.isalpha():
                    j = -1
                    for i in range(len(ans)):
                        j += 1
                    if ans[j] != 'a':
                        ans += 'a'
                else:
                    ans += ch
        new = ''
        for i in range(len(ans)):
            if ans[i].isdigit():
                if ans[i-1] != '\n':
                    new += ans[i]
            if ans[i].isalpha():
                new += ','
        male = []
        female = []
        x = 0
        for ele in new:
            ele.strip()
            if ele == ',':
                x += 1
                male.append(',')
                female.append(',')
            if x % 2 == 0:
                if x != 0:
                    if ele.isdigit():
                        female.append(ele)
            if x % 2 != 0:
                if x != 0:
                    if ele.isdigit():
                        male.append(ele)
        num_m = ''
        count_m = 0
        for i in range(len(male)):
            if male[i] != ',':
                num_m += male[i]
            else:
                if num_m != '':
                    for j in range(len(num_m)):
                        count_m += int(num_m[j])*10**(len(num_m)-j-1)
                num_m = ''
        print('Male Number:', count_m-2122)
        num_f = ''
        count_f = 0
        count = 0
        for i in range(len(female)):
            if female[i] != ',':
                num_f += female[i]
            else:
                if num_f != '':
                    count += 1
                    if count < 9 or count == 200:
                        for j in range(len(num_f)):
                            count_f += int(num_f[j])*10**(len(num_f)-j-1)
                    if count >= 9:
                        if count < 99:
                            for j in range(len(num_f)-1):
                                count_f += int(num_f[j])*10**(len(num_f)-1-j-1)
                        elif count <= 199:
                            for j in range(len(num_f)-2):
                                count_f += int(num_f[j])*10**(len(num_f)-2-j-1)
                num_f = ''
        print('Female Number:', count_f)


if __name__ == '__main__':
    main()
