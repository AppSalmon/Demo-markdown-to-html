from flask import Flask, render_template, request
import pypandoc

app = Flask(__name__)

# Tải và cài đặt Pandoc tự động
pypandoc.download_pandoc()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        markdown_text = request.form['markdown']

        print(markdown_text)
        
        # Chuyển đổi từ chuỗi Markdown sang HTML
        html_output = pypandoc.convert_text(markdown_text, 'html', format='md')
        return render_template('result.html', html_output=html_output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
