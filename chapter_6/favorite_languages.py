languages = {
	'jen':'python',
	'nick':'java',
	'alex':'python',
	'gabby':'c++',
	'hank':'javascript',
	'mike':'python'
}

targeted_people = ['mike','steve','chris','alex','bill']

for i in targeted_people:
	if i in languages:
		print(f"Thank you for taking the poll {i.title()}!")
	else:
		print(f"Please take the poll {i.title()}!")