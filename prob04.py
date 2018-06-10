import re
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""
def remove_tag(s):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', s)
    return cleantext
print(remove_tag(s))
'''
실행 결과: 


    
        Click
        Here
        
        	     To connect to the most powerful tools  in the world.
        


'''
