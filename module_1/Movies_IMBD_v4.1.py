#!/usr/bin/env python
# coding: utf-8

# In[112]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# In[113]:


data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)


# In[114]:


data.describe()


# # Предобработка

# In[115]:


# создадим словарь для ответов
answers
# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...

# for task 6: calculate movie profit by substracting budget from revenue and add separate column for 'profit' 
data['profit']=data.revenue-data.budget

# for task 11: in order to determine most popular genre let's use Counter container 
import collections
g=collections.Counter()
e=data.genres # we need to work with 'genres' column
for line in e:
    info=line.split('|') # genres are separated with '|' so we need to split them
    gnr=info[0]
    g[gnr]+=1


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[116]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '5. Pirates of the Caribbean: On Stranger Tides (tt1298650)'
# если ответили верно, можете добавить комментарий со значком "+"


# In[157]:


# тут пишем ваш код для решения данного вопроса:
data[['original_title','budget']].sort_values('budget',ascending=False).head()


# ВАРИАНТ 2

# In[18]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[117]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = '2. Gods and Generals (tt0279111)'


# In[159]:


data[['original_title','runtime']].sort_values('runtime',ascending=False).head()


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[118]:


answers['3'] = '3. Winnie the Pooh (tt1449283)'


# In[161]:


data[['original_title','runtime']].sort_values('runtime').head()


# # 4. Какова средняя длительность фильмов?
# 

# In[119]:


answers['4'] = '2. 110'


# In[77]:


data.runtime.mean()


# # 5. Каково медианное значение длительности фильмов? 

# In[120]:


answers['5'] = '1. 107'


# In[81]:


data.runtime.median()


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[121]:


# лучше код получения столбца profit вынести в Предобработку что в начале
answers['6'] = '5. Avatar (tt0499549)'


# In[162]:


data[['imdb_id','original_title','profit']].sort_values('profit',ascending=False).head()


# # 7. Какой фильм самый убыточный? 

# In[122]:


answers['7'] = '5. The Lone Ranger (tt1210819)'


# In[163]:


data[['imdb_id','original_title','profit']].sort_values('profit').head()


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[123]:


answers['8'] = '1. 1478'


# In[126]:


len(data[data.profit>0])


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[124]:


answers['9'] = '4. The Dark Knight (tt0468569)'


# In[165]:


data.query('release_year=="2008"').sort_values('revenue',ascending=False)[['imdb_id','original_title','revenue']].head()


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[125]:


answers['10'] = '5. The Lone Ranger (tt1210819)'


# In[167]:


data.query('2012<=release_year<=2014').sort_values('profit')[['imdb_id','original_title','profit']].head()


# # 11. Какого жанра фильмов больше всего?

# In[126]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале
answers['11'] = '3. Drama'


# In[4]:


data['genres'].str.cat(sep='|')
pd.Series(data['genres'].str.cat(sep='|').split('|'))
pd.Series(data['genres'].str.cat(sep='|').split('|')).value_counts()


# ВАРИАНТ 2

# In[11]:





# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[127]:


answers['12'] = '1. Drama'


# In[25]:


data2=data[data.profit>0]
data2['genres'].str.cat(sep='|')
pd.Series(data2['genres'].str.cat(sep='|').split('|'))
pd.Series(data2['genres'].str.cat(sep='|').split('|')).value_counts()


# # 13. У какого режиссера самые большие суммарные кассовые сбооры?

# In[128]:


answers['13'] = '5. Peter Jackson'


# In[52]:


rev_dir=data.pivot_table(values='revenue',
                index='director',
                aggfunc='sum',
                        fill_value=0)
rev_dir.sort_values('revenue',ascending=False).head()


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[129]:


answers['14'] = '3. Robert Rodriguez'


# In[66]:


data['list_dirs']=data.director.str.split('|')
data_action=data[data.genres.str.contains('Action')][['list_dirs']]
data_exploided_action=data_action.explode('list_dirs')
data_exploided_action.list_dirs.value_counts()


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[130]:


answers['15'] = '3. Chris Hemsworth'


# In[101]:


data['list_cast']=data.cast.str.split('|')
data_year=data.query('release_year in ["2012"]')
data_exploided_year=data_year.explode('list_cast')
ef=data_exploided_year.pivot_table(values='revenue',
                               index='list_cast',
                               aggfunc='sum',
                               fill_value=0)
ef.sort_values('revenue',ascending=False)


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[131]:


answers['16'] = '3. Matt Damon'


# In[97]:


data['list_cast']=data.cast.str.split('|')
data_budget=data[data.budget>data.budget.mean()]
data_exploded_budget=data_budget.explode('list_cast')
tn=data_exploded_budget.pivot_table(values='imdb_id',
                                    index='list_cast',
                                    aggfunc='count',
                                    fill_value=0)
tn.sort_values('imdb_id',ascending=False)


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[132]:


answers['17'] = '2. Action'


# In[22]:


data['list_cast']=data.cast.str.split('|')
data['new_genres']=data.genres.str.split('|')
cage=data[data.cast.str.contains('Nicolas Cage')]
expl=cage.explode('new_genres')
cage_count=expl.pivot_table(values='imdb_id',
                index='new_genres',
                aggfunc='count',
                fill_value=0)
cage_count.sort_values('imdb_id',ascending=False)


# # 18. Самый убыточный фильм от Paramount Pictures

# In[133]:


answers['18'] = '1. K-19: The Widowmaker (tt0267626)'


# In[169]:


data[(data.production_companies.str.contains('Paramount Pictures'))&(data.profit<0)].sort_values('profit').head(1)


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[134]:


answers['19'] = '5. 2015'


# In[170]:


success=data.pivot_table(values='revenue',
                index='release_year',
                aggfunc='sum',
                fill_value=0)
success.sort_values('revenue',ascending=False).head()


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[135]:


answers['20'] = '1. 2014'


# In[171]:


data_warner=data[data.production_companies.str.contains('Warner Bros')]
good_year=data_warner.pivot_table(values='profit',
                       index='release_year',
                       aggfunc='sum',
                       fill_value=0)
good_year.sort_values('profit',ascending=False).head()


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[136]:


answers['21'] = '4. Сентябрь'


# In[137]:


data['release_date'] = pd.to_datetime(data['release_date'])
data.release_date.dt.month.value_counts()


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[137]:


answers['22'] = '2. 450'


# In[153]:


data['release_date'] = pd.to_datetime(data['release_date'])
len(data[(data.release_date.dt.month==6)|(data.release_date.dt.month==7)|(data.release_date.dt.month==8)])


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[138]:


answers['23'] = '5. Peter Jackson'


# In[41]:


data['release_date'] = pd.to_datetime(data['release_date'])
data['month']=data.release_date.dt.month
data['list_dirs']=data.director.str.split('|')
data_winter=data[(data.month==12)|(data.month==1)|(data.month==2)][['list_dirs']]
data_exploded_winter=data_winter.explode('list_dirs')
data_exploded_winter.list_dirs.value_counts()


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[139]:


answers['24'] = '5. Four By Two Productions'


# In[95]:


def counter(movie_bd, x):
    data_plot=movie_bd[x].str.cat(sep='|')
    dat=pd.Series(data_plot.split('|'))
    info=dat.value_counts(ascending=False)
    return info
data['title_words_length'] = data.original_title.map(lambda x: len(x.split(' ')))
sum_gen=counter(data,'production_companies')
for gen in sum_gen.index:
    sum_gen[gen] = data['title_words_length'][data['production_companies'].map(lambda x: True if gen in x else False)].mean()
sum_gen = pd.DataFrame(sum_gen).sort_values(0, ascending=False)


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[140]:


answers['25'] = '3. Midnight Picture Show'


# In[101]:


def counter(movie, x):
    data1=movie[x].str.cat(sep='|')
    data2=pd.Series(data1.split('|'))
    info=data2.value_counts(ascending=False)
    return info
data['word'] = data.overview.str.split().map(len)
summ = counter(data,'production_companies')
for i in summ.index:
    summ[i] = data['word'][data['production_companies'].map(lambda x: True if i in x else False)].mean()
summ = pd.DataFrame(summ).sort_values(0, ascending=False)


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# 
# по vote_average

# In[141]:


answers['26'] = '1. Inside Out, The Dark Knight, 12 Years a Slave'


# In[79]:


data[['original_title','vote_average']].sort_values('vote_average',ascending = False).head(int(len(data['vote_average'])*0.01))


# ВАРИАНТ 2

# In[174]:


top_1_vote = data[data['vote_average'] > data['vote_average'].quantile(0.99)][['vote_average','original_title']].sort_values('vote_average',ascending=False)
display(top_1_vote)


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# In[143]:


answers['27'] = '5. Daniel Radcliffe & Rupert Grint'


# In[175]:


from itertools import combinations
actor_list = data.cast.str.split('|').tolist()
combo_list=[]
for i in actor_list:
   for j in combinations(i, 2):
       combo_list.append(' '.join(j))
combo_list = pd.DataFrame(combo_list)
combo_list.columns = ['actor_combinations']
combo_list.actor_combinations.value_counts().head(10)


# # Submission

# In[176]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[177]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[ ]:





# In[ ]:




