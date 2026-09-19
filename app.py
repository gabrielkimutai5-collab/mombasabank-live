from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MombasaBank</title>
<style>
*{margin:0;padding:0;box-sizing:border-box} body{font-family:Arial;background:#eef4ff;color:#0a2a4a}
.top{background:#0a2a4a;color:white;padding:16px 20px;display:flex;justify-content:space-between}
.logo{font-weight:900;font-size:22px} .logo b{color:#ffcc66}
.card-main{background:linear-gradient(135deg,#0d47a1,#0a2a4a);color:white;border-radius:22px;padding:28px;margin:18px}
.amount{font-size:36px;font-weight:900;margin:10px 0}
.btn{background:#ffcc66;color:#0a2a4a;border:none;padding:11px 20px;border-radius:30px;font-weight:800;margin:5px;cursor:pointer}
.box{background:white;border-radius:16px;padding:18px;box-shadow:0 4px 10px rgba(0,0,0,.07);margin:10px}
.ussd{background:#ffcc66;border-radius:14px;padding:16px;text-align:center;cursor:pointer}
.code{font-size:28px;font-weight:900}
</style>
</head>
<body>
<div class="top"><div class="logo">Mombasa<b>Bank</b></div><div>LIVE</div></div>
<div class="card-main">
<div>Salio Lako</div>
<div class="amount">KES 126,450.00</div>
<button class="btn" onclick="alert('Feature inakuja!')">Ongeza Pesa</button>
<button class="btn" style="background:transparent;border:1px solid #ffcc66;color:white" onclick="alert('Taarifa: Salio lako ni KES 126,450')">Taarifa</button>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0;padding:0 8px">
<div class="box"><h3>Tuma Pesa</h3><p style="margin:12px 0">Neema • Jabari • Fatma</p><button class="btn" style="width:100%;background:#0a2a4a;color:white" onclick="alert('Tuma Pesa - Feature inakuja')">Tuma Sasa</button></div>
<div class="box"><h3>USSD - Bila Mtandao</h3><div class="ussd" onclick="alert('Piga: *384*19031# kwenye simu yako')"><div class="code">*384*19031#</div><div style="font-size:11px">Gusa ku-copy - Piga kwa simu</div></div><p style="font-size:12px;margin-top:10px">Hii haifungui ukurasa, ni namba ya kupiga tu.</p></div>
</div>
<div style="text-align:center;padding:20px;font-size:11px;opacity:.6">© 2026 MombasaBank | ONLINE LIVE</div>
<script>console.log('MombasaBank Loaded OK');</script>
</body>
</html>
"""

@app.route('/ussd', methods=['POST','GET'])
def ussd():
    session_id = request.values.get("sessionId","")
    phone = request.values.get("phoneNumber","")
    text = request.values.get("text","")
    # Safisha text
    text = text.strip()
    print(f"USSD HIT: {phone} -> {text}")
    if text == "":
        resp = "CON Karibu MombasaBank\n1. Salio Langu\n2. Tuma Pesa\n3. Mkopo Haraka\n0. Toka"
    elif text == "1":
        resp = "END Salio Lako: KES 12,500\nAsante kutumia MombasaBank!"
    elif text == "2":
        resp = "CON Weka namba:\n"
    elif text.startswith("2*"):
        resp = "END Umeomba kutuma. Tutakujulisha!"
    elif text == "3":
        resp = "END Mkopo: Unastahili hadi KES 50,000. Piga *384*19031# tena"
    else:
        resp = "END Chaguo batili. Karibu tena!"
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
