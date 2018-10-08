import statsmodels.api as sm

x_array = x.as_matrix(columns=None)
y_array = y.as_matrix(columns=None)        
ols_result = sm.OLS(y_array, x_array).fit() # fit是一个结果，也是一个接口，可以通过这个接口调用想看的数据
wls_model = sm.WLS(y_array, x_array, weights=list(weight)) # weight这个公式里面会自动开根

# 常用的参数如下：
ols_resid = sm.OLS(y_array, x_array).fit().resid #残差
ols_resid = sm.OLS(y_array, x_array).fit().tvalues 
ols_resid = sm.OLS(y_array, x_array).fit().params #系数
ols_resid = sm.OLS(y_array, x_array).fit().bse #standard error
