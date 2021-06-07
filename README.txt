feature_picker(model, features, threshold)

model -- This parameter will be the model you are using that has already been fit with the data.
i.e. 
log = LinearRegression()
log.fit(x_train, y_train)

In this case, "log" would be inputted for this parameter.


features -- This paramter will be the list of all the features that are in the data set you are using
i.e.
x = df[['sex', 'cp', 'fbs', 'restecg', 'exng', 'oldpeak', 'caa', 'thall']]

In this case, "x" would be inputted for this parameter.



threshold -- This parameter would be the LOWEST acceptable coeffecient you want to accept for your model.
i.e.
.2 would be inputted for this parameter.
The algorithm will go through the coeffeciants of all the features in the list associated with the "features" parameter and pick out all of the features that have a coefficient of
.2 or HIGHER.

NOTE: When selecting a threshold, it will accept coefficients with negatives as well.
For example: if the set threshold is .2, the function will return features with a coefficient less than or equal to -.2


The function should be called after all of these variable have already been established.
The function will return a dictionary with a key:value pair of feature:coef