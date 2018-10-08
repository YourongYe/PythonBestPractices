# get industry dummy variables
industry_LevelDict = {1:Banking;2:Food} # sample dictionary
industry['Industry'] = industry['Industry'].map(industry_LevelDict)
industry['Industry'].drop_duplicates()
dummies = pd.get_dummies(industry, columns=['Industry'],prefix=['Industry'],prefix_sep="_",dummy_na=False,drop_first=False)
