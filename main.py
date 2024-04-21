from flask import Flask, render_template, request
import calculator

# Define Flask app object
app = Flask(__name__)

# Define how Flask app should handle root URL "/"
@app.route("/", methods=["GET", "POST"])
def fun():
    # Check if a submit button has been pressed on HTML page
    if request.method == "POST":
        # Loop through all calculator buttons to find which submit button was pressed on HTML page
        # (calculator button "1" is called "button_1" on HTML page etc.)
        for button in calculator.button_set:
            if request.form.get("button_"+button):
                # Send pressed button to calculator, so it can update its display accordingly
                calculator.press_button(button)

    # (Re)render HTML page with fresh calculator display
    return render_template("index.html", calculator_display=calculator.display)


# Run the Flask app and tell it to use port 5001 (debug=True can be removed)
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)