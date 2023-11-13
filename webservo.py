from flask import Flask, request, render_template
import atexit
import RPi.GPIO as GPIO

app = Flask(__name__)

# 初期状態では角度を0に設定
angle = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global angle  # state変数をグローバル変数として使用

    # GPIOの14番ポートを出力に設定
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    servo = GPIO.PWM(2, 50)
    servo.start(0.0)
    atexit.register(GPIO.cleanup)  # 終了時にcleanupを実行

    if request.method == 'POST':
        # フォームが送信された場合
        angle = request.form['servodeg']
        
        #サーボを駆動

     
    # フォームを表示
    return render_template('webservo.html', angle=angle)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

