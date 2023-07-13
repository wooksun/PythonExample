#!/usr/bin/env python
# coding: utf-8

# selection sort(선택정렬, 교환법) 알고리즘
# 
# 선택 정렬은 i번째 데이터를 선택해서 나머지 데이터(j번째)와 비교하며 정렬한다.  
# 정렬할 데이터가 n개일 경우 회전수는 n-1번이 된다. => 데이터가 5개면 회전수는 4번이다.  
# <img src="./selectionSort1.png" width="900" align="left"/>  
# 
# <img src="./selectionSort2.png" width="900" align="left"/>  
# 
# <img src="./selectionSort3.png" width="1200" align="left"/>  

# In[6]:


'''
n = 5
for i in range(n - 1):
    for j in range(i + 1, n):
        print(f'[i = {i}, j = {j}]', end='')
    print()
'''


# In[7]:


def selectionSortAsc(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            # 오름차순 정렬 => 앞(i번째)의 데이터가 뒤(j번째)의 데이터보다 크면 데이터를 교환한다.
            # 내림차순 정렬 => 앞(i번째)의 데이터가 뒤(j번째)의 데이터보다 작으면 데이터를 교환한다.
            # 부등호를 '>'에서 '<'로 변경하면 내림차순으로 정렬된다.
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
            # ===== if
        # ===== for j => 회전종료
        #print(f'{i + 1}회전 결과: {data}')
    # ===== for i => 회전종료
    #print(f'정렬결과: {data}')
    return data


# In[8]:


def selectionSortDesc(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            # 위와 부등호 차이로 내림차순이 됨
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    return data


# In[10]:


if __name__ == '__main__':
    data = [8, 3, 4, 9, 1]
    result = selectionSortAsc(data)
    print('정렬 결과: {}'.format(result))
    result = selectionSortDesc(data)
    print('정렬 결과: {}'.format(result))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




