from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MombasaBank</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Arial;background:#eef4ff;color:#0a2a4a}
.top{background:#0a2a4a;color:white;padding:16px 20px;display:flex;justify-content:space-between}
.logo{font-weight:900;font-size:22px} .logo b{color:#ffcc66}
.card-main{background:linear-gradient(135deg,#0d47a1,#0a2a4a);color:white;border-radius:22px;padding:28px;margin:18px}
.amount{font-size:36px;font-weight:900;margin:10px 0}
.btn{background:#ffcc66;color:#0a2a4a;border:none;padding:11px 20px;border-radius:30px;font-weight:800;margin:5px}
.btn2{background:transparent;color:white;border:1.5px solid #ffcc66;padding:11px 20px;border-radius:30px;font-weight:700}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;padding:0 18px}
.box{background:white;border-radius:16px;padding:18px;box-shadow:0 4px 10px rgba(0,0,0,.07)}
.ussd{background:linear-gradient(135deg,#ffcc66,#ffdb8a);border-radius:14px;padding:16px;text-align:center;margin-top:12px}
.code{font-size:28px;font-weight:900}
.quick{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}
.quick div{background:#e8efff;padding:12px;border-radius:12px;text-align:center;font-weight:600;font-size:14px}
.foot{text-align:center;padding:20px;font-size:11px;opacity:.6}
</style>
</head>
<body>
<div class="top"><div class="logo">⛵ Mombasa<b>Bank</b></div><div>EN | SWA</div></div>

<div class="card-main">
<div>Salio Lako • Available Balance</div>
<div class="amount">KES 126,450.00</div>
<div>↑ +KES 12,300 kutoka mwezi uliopita</div><br>
<button class="btn">Ongeza Pesa</button>
<button class="btn2">Taarifa</button>
</div>

<div class="grid">
<div class="box">
<h3>Tuma Pesa</h3>
<div style="display:flex;justify-content:space-around;margin:14px 0"><div>👩<br>Neema</div><div>👨<br>Jabari</div><div>👩<br>Fatma</div></div>
<button class="btn" style="width:100%;background:#0a2a4a;color:white">Tuma Sasa →</button>
</div>

<div class="box">
<h3>USSD • Bila Mtandao</h3>
<div class="ussd" onclick="naviggator.clipboard.writeText('*384*19031#'); alert('USSD Copied: *384*19031# - Piga kwenye simu!')">
<div class="code">*384*19031#</div>
<div style="font-size:12px;margin-top:5px">Piga kwa huduma haraka bila internet</div>
</div>
</div>
</div>

<div class="box" style="margin:18px">
<h3>Huduma Haraka</h3>
<div class="quick">
<div>💧 Lipa Bills</div>
<div>📞 Airtime</div>
<div>💰 Omba Mkopo</div>
<div>⬇️ Pokea Pesa</div>
</div>
</div>

<div class="box" style="margin:18px">
<h3>Shughuli za Karibuni</h3>
<p>🛒 Leo 09:42 - Naivas <span style="float:right;color:red">-2,150</span></p>
<p style="margin-top:8px">⬇️ Jana 16:20 - Kutoka Jabari <span style="float:right;color:green">+5,000</span></p>
<p style="margin-top:8px">💡 18 Sept - Kenya Power <span style="float:right;color:red">-3,400</span></p>
</div>

<div class="foot">© 2026 MombasaBank | Licensed by CBK | Msaada: 0800 384 190<br><b style="color:green">● ONLINE LIVE</b> - mombasabank-live.onrender.com</div>
</body>
</html>
"""

@app.route('/ussd', methods=['POST','GET'])
def ussd():
    text = request.values.get("text","") or request.args.get("text","")
    if text == "":
        return "CON Karibu MombasaBank 🏦\n1. Salio\n2. Tuma Pesa\n3. Mkopo\n4. LUKU\n0. Toka"
    elif text == "1":
        return "END Salio Lako: KES 12,500. Asante!"
    elif text == "2":
        return "CON Weka namba ya kupokea:"
    else:
        return "END Asante kwa kutumia MombasaBank!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
