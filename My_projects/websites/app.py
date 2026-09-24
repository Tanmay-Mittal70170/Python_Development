from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'shopping_secret_key_123'  # Required for session/cart management

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Tanmay@123",  # Updated with your MySQL password
        database="shopping"
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("products.html", products=products)

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    # Get list of all checked product IDs
    selected_ids = request.form.getlist("product_ids")

    if not selected_ids:
        return redirect(url_for("products"))

    connection = connect_db()
    cursor = connection.cursor()

    cart = session.get("cart", [])

    for p_id in selected_ids:
        product_id = int(p_id)
        # Fetch individual product quantity from form
        quantity = int(request.form.get(f"quantity_{product_id}", 1))

        cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
        product = cursor.fetchone()

        if product:
            # Check if item is already in session cart
            for item in cart:
                if item["product_id"] == product_id:
                    item["quantity"] += quantity
                    break
            else:
                cart.append({
                    "product_id": product[0],
                    "name": product[1],
                    "price": float(product[3]),
                    "quantity": quantity
                })

    cursor.close()
    connection.close()

    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total = sum(item["price"] * item["quantity"] for item in cart_items)
    return render_template("cart.html", cart=cart_items, total=round(total, 2))

@app.route("/remove-from-cart", methods=["POST"])
def remove_from_cart():
    product_id = int(request.form.get("product_id"))
    cart = session.get("cart", [])
    cart = [item for item in cart if item["product_id"] != product_id]
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart_items = session.get("cart", [])
    if not cart_items:
        return redirect(url_for("products"))

    subtotal = sum(item["price"] * item["quantity"] for item in cart_items)
    gst = subtotal * 0.18
    discount = subtotal * 0.10
    final_total = subtotal + gst - discount

    if request.method == "POST":
        customer_name = request.form.get("customer_name")
        customer_mobile = request.form.get("customer_mobile")

        connection = connect_db()
        cursor = connection.cursor()

        # Save order to MySQL database
        cursor.execute(
            "INSERT INTO orders (customer_name, customer_mobile, total_price) VALUES (%s, %s, %s)",
            (customer_name, customer_mobile, final_total)
        )
        connection.commit()
        order_id = cursor.lastrowid

        # Save individual items to database
        for item in cart_items:
            cursor.execute(
                "INSERT INTO order_items (order_id, product_name, quantity, price) VALUES (%s, %s, %s, %s)",
                (order_id, item["name"], item["quantity"], item["price"])
            )
        connection.commit()
        cursor.close()
        connection.close()

        # Keep items list for receipt before clearing cart session
        purchased_items = list(cart_items)
        session["cart"] = []

        # Render the final bill page
        return render_template(
            "bill.html",
            order_id=order_id,
            customer_name=customer_name,
            customer_mobile=customer_mobile,
            items=purchased_items,
            subtotal=round(subtotal, 2),
            gst=round(gst, 2),
            discount=round(discount, 2),
            final_total=round(final_total, 2)
        )

    return render_template(
        "checkout.html",
        total=round(subtotal, 2),
        gst=round(gst, 2),
        discount=round(discount, 2),
        final_total=round(final_total, 2)
    )

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM admin_users WHERE username = %s AND password = %s", (username, password))
        admin = cursor.fetchone()
        cursor.close()
        connection.close()

        if admin:
            return f"<h2>Welcome Admin {username}! Login Successful.</h2><br><a href='/'>Go to Home</a>"
        else:
            return "<h2>Invalid Credentials. <a href='/admin/login'>Try Again</a></h2>"

    return render_template("admin_login.html")

if __name__ == "__main__":
    app.run(debug=True)