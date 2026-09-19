from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>MombasaBank LIVE! 🏦</h1><p>Pesa kwa Mkono<br>USSD: *384*19031#<br><b style='color:green'>ONLINE</b></p>"

@app.route('/ussd', methods=['POST','GET'])
def ussd():
    text = request.values.get("text","") or request.args.get("text","")
    if text == "":
        return "CON Karibu MombasaBank 🏦\n1. Salio\n2. Tuma Pesa\n3. Mkopo\n4. LUKU\n0. Toka"
    elif text == "1":
        return "END Salio lako: KES 12,500. Asante!"
    elif text == "2":
        return "END Tuma Pesa - Huduma inakuja!"
    elif text == "3":
        return "END Mkopo KES 5,000 umeidhinishwa!"
    else:
        return "END Asante kwa kutumia MombasaBank!"

if __name__ == "__main__":
    app.run()
