
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("E:\PYTHON FILE\Train.csv")
data.head()


# In[ ]:


#hitung jumlah total penumpang kapal
    #jumlah penumpang L dan P
    #umur rata-rata penumpang L dan P
    #siapa saja yang ada pada Pclass
        #jumlah laki-laki dan perempuan masing masing pclass
#jumlah penumpang selamat dan tidak selamat
    #jumlah penumpang selamat dan tidak selamat laki-laki dan perempuan
    #jumlah penumpang selamat dan tidak selamat berdasarkan kelas
        #dikelompokkan lagi berdasarkan jenis kelamin dan umur

#umur rata-rata penumpang per kelas
    #umur rata-rata penumpang perkelas dibagi menjadi laki-laki dan perempuan
    


# In[ ]:


#hitung jumlah total penumpang kapal
print("Jumlah Total Penumpang Kapal Titanic :",data["Name"].count())
print("Jumlah penumpang :","\n",data['Sex'].value_counts())


# In[ ]:


#umur rata-rata penumpang L dan P
print("Umur rata-rata penumpang Laki-Laki dan Perempuan :","\n",
      "Laki-Laki :",data[data.Sex=='male'].Age.mean(),"\n",
      "Perempuan :",data[data.Sex=='female'].Age.mean())


# In[ ]:


#nama siapa saja yang ada pada Pclass
inp = int(input ("Masukkan : "))
if inp == 1 :
    print(data[data.Pclass == 1].Name)
elif inp == 2 :
    print(data[data.Pclass==2].Name)
else :
    print(data[data.Pclass==3].Name)


# In[ ]:


#jumlah penumpang pada masing masing Pclass
print(data.groupby(['Pclass']).PassengerId.count())


# In[9]:


#jumlah laki-laki dan perempuan masing masing pclass
data.groupby(['Pclass','Sex']).Sex.count()


# In[15]:


print(data.Survived.value_counts(),"Ket : ","\n","0 = Tidak Selamat","\n","1 = Selamat","\n")


# In[19]:


#jumlah penumpang selamat dan tidak selamat laki-laki dan perempuan
data.groupby(['Survived', 'Sex']).Sex.count()


# In[28]:


#jumlah penumpang selamat dan tidak selamat berdasarkan kelas
data.groupby(['Survived','Pclass','Sex']).Pclass.count()


# In[30]:


bins = [10,30,50,70,90]
data ['Agebin'] = pd.cut (data['Age'],bins)


# In[31]:


data.groupby(['Survived','Pclass','Sex','Agebin']).Pclass.count()


# In[34]:


#umur rata-rata penumpang per kelas
data.groupby(['Pclass']).Age.mean()


# In[35]:


#umur rata-rata penumpang perkelas dibagi menjadi laki-laki dan perempuan
data.groupby(['Pclass','Sex']).Age.mean()

