import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    current_stocks = db.execute(
        "SELECT stock_name,stock_symbol,stock_count,price FROM current_stocks WHERE user_id = ?", session["user_id"])
    total_stock_value = 0
    cash = db.execute("SELECT cash FROM users WHERE id = ?",
                      session["user_id"])
    for stock in current_stocks:
        stock_info = lookup(stock["stock_symbol"])
        stock["current_price"] = stock_info["price"] * stock["stock_count"]
        stock["each_stock"] = stock_info["price"]
        total_stock_value += stock["current_price"]
    total_value = float(total_stock_value) + float(cash[0]["cash"])
    return render_template("index.html", current_stocks=current_stocks, total_stock_value=total_stock_value, cash=cash[0]["cash"], total_value=total_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("symbol"):
            return apology("must provide a valid stock symbol", 400)

        # Ensure password was submitted
        elif not request.form.get("shares"):
            return apology("must provide a valid quantity of shares to buy", 400)

        elif request.form.get("shares").isdigit() == False:
            return apology("must provide a valid quantity of shares to buy", 400)

        elif float(request.form.get("shares")) <= 0:
            return apology("provide a valid share input", 400)

        elif (float(request.form.get("shares")) % 1) != 0:
            return apology("provide a valid share input", 400)

        stock = lookup(request.form.get("symbol"))
        current_cash_dict = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"])
        current_cash = current_cash_dict[0]["cash"]
        if stock == None:
            return apology("Invalid Stock name", 400)

        elif stock["price"]*int(request.form.get("shares")) > current_cash:
            return apology("Not Enough Balance", 400)

        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash -
                   (stock["price"]*int(request.form.get("shares"))), session["user_id"])
        current_stock_existence = db.execute(
            "SELECT * FROM current_stocks WHERE stock_symbol = ? AND user_id = ?", stock["symbol"], session["user_id"])
        if len(current_stock_existence) != 0:
            current_stock_count_dict = db.execute(
                "SELECT stock_count FROM current_stocks WHERE stock_symbol = ? AND user_id = ?", stock["symbol"], session["user_id"])
            current_stock_price_dict = db.execute(
                "SELECT price FROM current_stocks WHERE stock_symbol = ? AND user_id = ?", stock["symbol"], session["user_id"])
            current_stock_count = current_stock_count_dict[0]["stock_count"]
            current_stock_price = current_stock_price_dict[0]["price"]
            db.execute("UPDATE current_stocks SET stock_count = ?, price = ? WHERE stock_symbol = ? AND user_id = ?", current_stock_count + int(
                request.form.get("shares")), current_stock_price + (stock["price"] * int(request.form.get("shares"))), stock["symbol"], session["user_id"])
            db.execute("INSERT INTO stocks_history(stock_name,stock_count,stock_symbol,user_id,time,price,transaction_type) VALUES(?,?,?,?,datetime('now'),?,'BOUGHT')",
                       stock["name"], int(request.form.get("shares")), stock["symbol"], session["user_id"], stock["price"] * int(request.form.get("shares")))

        else:
            db.execute("INSERT INTO current_stocks(stock_name,stock_count,stock_symbol,user_id,price) VALUES(?,?,?,?,?)", stock["name"], request.form.get(
                "shares"), stock["symbol"], session["user_id"], stock["price"] * int(request.form.get("shares")))
            db.execute("INSERT INTO stocks_history(stock_name,stock_count,stock_symbol,user_id,time,price,transaction_type) VALUES(?,?,?,?,datetime('now'),?,'BOUGHT')",
                       stock["name"], request.form.get("shares"), stock["symbol"], session["user_id"], stock["price"] * int(request.form.get("shares")))

        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    stock_history = db.execute(
        "SELECT stock_name, stock_count, time, stock_symbol, price, transaction_type FROM stocks_history WHERE user_id = ?", session["user_id"])
    return render_template("history.html", stock_history=stock_history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        # Ensures if stock name is submitted
        if not request.form.get("symbol"):
            return apology("must provide a Stock Name", 400)

        # ensures if stock name is valid
        stock = lookup(request.form.get("symbol"))
        if stock == None:
            return apology("Invalid Stock name", 400)

        return render_template("quoted.html", stock=stock)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Password did not matched", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # checks for any existing same username
        if len(rows) != 0:
            return apology("Username already Taken", 400)

        # registers user into database
        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", request.form.get(
            "username"), generate_password_hash(request.form.get("password")))

        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("registration.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("symbol"):
            return apology("must provide a valid stock symbol", 400)

        # Ensure password was submitted
        elif not request.form.get("shares"):
            return apology("must provide a valid quantity of shares to buy", 400)

        elif (request.form.get("shares").isdigit() == False):
            return apology("must provide a valid quantity of shares to buy", 400)

        elif int(request.form.get("shares")) < 0:
            return apology("must provide a valid quantity of shares to buy", 400)

        '''elif (float(request.form.get("shares")) % 1) != 0:
            return apology("provide a valid share input",400)
        '''
        stock = lookup(request.form.get("symbol"))
        current_cash_dict = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"])
        current_cash = float(current_cash_dict[0]["cash"])
        if stock == None:
            return apology("Invalid Stock name", 400)

        current_stock_existence = db.execute(
            "SELECT * FROM current_stocks WHERE stock_symbol = ? AND user_id = ?", stock["symbol"], session["user_id"])
        stock_check = current_stock_existence[0]["stock_count"]
        if len(current_stock_existence) != 0 and stock_check >= int(request.form.get("shares")):
            current_stock_count_dict = db.execute(
                "SELECT stock_count FROM current_stocks WHERE stock_symbol = ? AND user_id = ?", stock["symbol"], session["user_id"])
            current_stock_price_dict = db.execute(
                "SELECT price FROM current_stocks WHERE stock_symbol = ? AND user_id = ?", stock["symbol"], session["user_id"])
            current_stock_count = int(
                current_stock_count_dict[0]["stock_count"])
            current_stock_price = float(current_stock_price_dict[0]["price"])
            db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash +
                       (stock["price"]*int(request.form.get("shares"))), session["user_id"])
            if current_stock_count - int(request.form.get("shares")) == 0:
                db.execute("DELETE FROM current_stocks WHERE stock_symbol = ? AND user_id = ?",
                           stock["symbol"], session["user_id"])
            else:
                db.execute("UPDATE current_stocks SET stock_count = ?, price = ? WHERE stock_symbol = ? AND user_id = ?", current_stock_count - int(request.form.get("shares")),
                           (float(current_stock_price)/float(current_stock_count)) * (current_stock_count - int(request.form.get("shares"))), stock["symbol"], session["user_id"])
            db.execute("INSERT INTO stocks_history(stock_name,stock_count,stock_symbol,user_id,time,price,transaction_type) VALUES(?,?,?,?,datetime('now'),?,'SOLD')",
                       stock["name"], request.form.get("shares"), stock["symbol"], session["user_id"], stock["price"] * int(request.form.get("shares")))

        else:
            return apology("You do not have this share in your portfolio", 400)

        return redirect("/")

    else:
        symbols = db.execute(
            "SELECT stock_symbol FROM current_stocks WHERE user_id = ?", session["user_id"])
        return render_template("sell.html", symbols=symbols)
