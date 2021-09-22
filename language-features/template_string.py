from string import Template

def main():
	str1 = "you're watching {0} by {1}".format("advanced python", "joe marini")
	print(str1)

	templ = Template("you're watching ${title} by ${author}")

	str2 = templ.substitute(title="advanced python", author="joe marini")
	print(str2)

	data = {
		"author": "joe marini",
		"title": "advanced python"
	}

	str3 = templ.safe_substitute(data)
	print(str3)

if __name__ == "__main__":
	main()
