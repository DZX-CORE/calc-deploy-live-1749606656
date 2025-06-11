from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """<!DOCTYPE html>
<html><head><title>Calculadora Online</title>
<style>
body{font-family:Arial;text-align:center;background:#f0f0f0;padding:20px}
.calc{background:white;padding:30px;border-radius:10px;max-width:350px;margin:0 auto;box-shadow:0 5px 15px rgba(0,0,0,0.1)}
input{width:80%;padding:10px;margin:5px;border:1px solid #ddd;border-radius:5px;font-size:16px}
button{padding:10px 20px;margin:5px;border:none;background:#007bff;color:white;border-radius:5px;cursor:pointer;font-size:14px}
button:hover{background:#0056b3}
#result{background:#e9ecef;padding:15px;margin:15px 0;border-radius:5px;font-weight:bold}
.status{background:#28a745;color:white;padding:8px;border-radius:3px;margin-bottom:15px}
</style></head>
<body>
<div class="calc">
<h2>Calculadora Web</h2>
<div class="status">DEPLOY REAL ATIVO</div>
<input type="number" id="a" placeholder="Número 1">
<input type="number" id="b" placeholder="Número 2">
<br>
<button onclick="calc('+'))">+</button>
<button onclick="calc('-'))">-</button>
<button onclick="calc('*'))">×</button>
<button onclick="calc('/'))">÷</button>
<div id="result">Digite números e clique em uma operação</div>
<small>Criado pelo orquestrador DZX-CORE</small>
</div>
<script>
function calc(op){
let a=parseFloat(document.getElementById('a').value);
let b=parseFloat(document.getElementById('b').value);
if(isNaN(a)||isNaN(b)){document.getElementById('result').innerHTML='Digite números válidos';return;}
let r;
switch(op){
case '+':r=a+b;break;
case '-':r=a-b;break;
case '*':r=a*b;break;
case '/':r=b!==0?a/b:'Erro: divisão por zero';break;
}
document.getElementById('result').innerHTML=a+' '+op+' '+b+' = '+r;
}
</script>
</body></html>"""

@app.route("/status")
def status():
    return {"status":"online","app":"calculadora","deploy":"real"}

if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
