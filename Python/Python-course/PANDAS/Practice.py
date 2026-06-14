import pandas as pd;
import numpy as np;

# s1= pd.Series(["ahsan","karak","software-engineer","khattak"],index = ["name","District","Profession","Caste"])
# print(s1)

# print(s1.iloc[3])

# s2 = pd.Series({"name":"Ahsanulhaq","District": "Karak","tehsil":"karak"})
# print(s2)
# print(s2["tehsil"])

# s3 = pd.Series({"s1":40,"s2":50,"s3":60,"s4":60,"s5":70})

# print(s3[s3<50])

# df1 = pd.DataFrame(np.arange(1,7).reshape(2,3),columns=[1,2,3],index=['a','b'])
# print(df1)
# print(df1[1])
# df1.columns = list("abc")
# df1.index = list("12")
# print(df1.index)

# s4 = pd.Series(np.random.randn(5),index = [1,2,3,4,5])
# s5 = pd.Series(np.random.randn(5), index = [1,2,3,4,5])

# df2 = pd.concat([s4,s5],axis = 1).abs()
# print(df2)
# print(df2[1])

# print(s4.to_frame())


df3 = pd.DataFrame(np.random.randn(25).reshape(5,5) , index = list("abcde"),columns=["col1","col2","col3","col4","col5"])

print(df3)


# print(df3.loc['c']['col3'])
print(df3.iloc[0,1])