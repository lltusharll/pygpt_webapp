import flask
import transformers

# Initialize the GPT-2 model
model = transformers.GPT2Model.from_pretrained('gpt2')

# Set up the Flask app
app = flask.Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
  return flask.render_template('index.html')

# Define the route for handling user input
@app.route('/generate', methods=['POST'])
def generate():
  input_text = flask.request.form['input_text']
  # Use the GPT-2 model to generate output based on the input text
  output_text = model.generate(input_text)
  return output_text

# Run the app
if __name__ == '__main__':
  app.run()
