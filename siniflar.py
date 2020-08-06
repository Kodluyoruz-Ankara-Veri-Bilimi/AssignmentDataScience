

class DataInformation:
    
    def __init__(self,data):
        print(data.info())
        print("*******************************")
        print(data.describe().T)
        print("*******************************")
        print("Nan variable sum = {}".format(data.isna().sum().sum()))
        
class Manipulation:
    def __init__(self):
        print("Manipülasyon İşlemleri...")
      
    def Manipulate(data):
        data=data.dropna(axis=0,how="any")
        return data
      
    
class Visualation():
      
    def __init__(self):
        print("Veri Görselleştirme İşlemleri...")
         
    def HistogramveKutu(var,data):
        import seaborn as sns
        import matplotlib.pyplot as plot
        fig, ax = plot.subplots(1,2, figsize = (10, 5))
        sns.distplot(data[var],ax=ax[0])
        sns.boxplot(data[var],ax=ax[1])
        
class modelOfStats():
    def __init__(self):
        print("OLS İşlemleri...")
        
    def lojistic(X,y):
        import statsmodels.api as sm 
        loj=sm.Logit(y,X)
        lojModel=loj.fit()
        print(lojModel.summary())
        return lojModel
    
      
class modelOfReg():
    def __init__(self):
        print("Regresyon İşlemleri...")
        
    def reg(x,y):
        from sklearn.linear_model import LogisticRegression
        model=LogisticRegression(solver='liblinear')
        loj_model=model.fit(x,y)
        return loj_model
    
     
    
        
        
    
