from flask import Flask, request, render_template
import atexit
import RPi.GPIO as GPIO

app = Flask(__name__)

# 初期状態では変数stateに空の文字列を保存
state = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global state  # state変数をグローバル変数として使用

    # GPIOの14番ポートを出力に設定
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    atexit.register(GPIO.cleanup)  #終了時にGPIO.cleanupを実行

    if request.method == 'POST':
        # フォームが送信された場合
        if request.form['action'] == 'on':
            GPIO.output(14, GPIO.HIGH)
            state = "on"
        elif request.form['action'] == 'off':
            GPIO.output(14, GPIO.LOW)
            state = "off"

    # フォームを表示
    return render_template('webled.html', state=state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

