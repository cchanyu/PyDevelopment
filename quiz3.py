# creates a site for new pw

# rule 1: remove http:// => naver.com
# rule 2: delete dot and after => naver
# rule 3: first 3 char(nav) + char count(5) + char e count(1) + !(!)
# ex pw: nav51!

userinput = "http://www.naver.com"
newpw = ""

temp = userinput.replace("http://", "")
print(temp)

if(temp.find("www.") > -1):
    temp = temp.replace("www.", "")

temp = temp[:temp.find(".")]
print(temp)

newpw = temp[:3] + str(len(temp)) + str(temp.count('e')) + "!"
print(newpw)


# NADOCODING'S SOLUTION
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")] 
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print("{0} password is {1}.".format(url, password))