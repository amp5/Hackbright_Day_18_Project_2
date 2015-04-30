"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken.
"""


from flask import Flask, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


import model

app = Flask(__name__)

# Need to use Flask sessioning features

app.secret_key = 'this-should-be-something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melons = model.Melon.get_all()
    return render_template("all_melons.html",
                           melon_list=melons)


@app.route("/melon/<int:id>")
def show_melon(id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = model.Melon.get_by_id(id)
    print melon
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart/", methods=["GET"])
def shopping_cart(id):
    """Display content of shopping cart."""

    # TODO: Display the contents of the shopping cart.
    #   - The cart is a list in session containing melons added

    # melon == an intance of the Melon class   
 

    melon = model.Melon.get_by_id(id)
    price = melon.price_str()
    quantity = 1
    print price
    return render_template("cart.html", melon_inst=melon, quantity=1,  price=price)




@app.route("/add_to_cart/<int:id>", methods=["GET"])
def add_to_cart(id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to cart'.
    """
    #Make a session

    # TODO: Finish shopping cart functionality
    #   - use session variables to hold cart list

    print session

    session["cart"] = session.get("cart", [])

    #we need to make it have an "if this is in this list, don't add it, append the current value
    # quantity.  IF it is not in the list, add it. 
    # the key is id and the value is quantity "

    melon = model.Melon.get_by_id(id)
    session["cart"].append(melon.id)
    
    # return redirect(url_for("shopping_cart"))


    melon = model.Melon.get_by_id(id)
    price = melon.price_str()
    quantity = 1
    print price
    return render_template("cart.html", melon_inst=melon, quantity=1,  price=price)

# problem redirecting to /cart not able to pull id from /add_to_cart
#use id numbers to add all this to our html cart


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!

    return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)
    app.run()