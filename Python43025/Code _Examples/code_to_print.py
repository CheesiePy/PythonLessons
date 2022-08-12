import webbrowser
f=open("index.html","w")
m="""
<html>
<head>
<style>
.animate-charcter
{
   text-transform: uppercase;
  background-image: linear-gradient(
    -225deg,
    #231557 0%,
    #44107a 29%,
    #ff1361 67%,
    #fff800 100%
  );
  background-size: auto auto;
  background-clip: border-box;
  background-size: 200px auto;
  color: #fff;
  background-clip: text;
  text-fill-color: transparent;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: textclip 2s linear infinite;
  display: inline-block;
      font-size: 100px;
}

@keyframes textclip {
  to {
    background-position: 100px center;
  }
}
</style>
</head>
<center>

<body>
  <div class="container">
  <div class="row">
    <div class="col-md-12 text-center">
      
      <h3 class="animate-charcter"> name:</h3>
      <h3 class="animate-charcter"> hearName </h3>
      <br>
      <h3 class="animate-charcter"> city:</h3>
      <h3 class="animate-charcter"> hearCity </h3>
      <br>
      <h3 class="animate-charcter"> age:</h3>
      <h3 class="animate-charcter"> hearAge </h3>
      
      <X09812>
    </div>
  </div>
</div>

</body>
</center>
</html>"""



name=input("my name ")#המשתמש הולך לכתוב את השם שלו
city=input("my city ")#המשתמש הולך לכתוב שאת העיר שלו
age=input("my age ")#המשתמש הולך לכתוב שאת הגיל שלו

m=m.replace("hearName",name)
m=m.replace("hearCity",city)
m=m.replace("hearAge",age)

f.write(m)
f.close()

webbrowser.open_new_tab('index.html')