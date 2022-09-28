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
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("stocksymbol"):
            return apology("must provide a valid stock symbol", 403)

        # Ensure password was submitted
        elif not request.form.get("numberofshares") or request.form.get("numberofshares")<=0:
            return apology("must provide a valid quantity of shares to buy", 403)

        stock = lookup(request.form.get("stocksymbol"))
        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        if stock == None:
            return apology("Invalid Stock name", 403)

        elif stock["price"]*request.form.get("numberofshares") > current_cash:
            return apology("Not Enough Balance", 403)

        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash - (stock["price"]*request.form.get("numberofshares")),session["user_id"])
        current_stock_existence = db.execute("SELECT count(*) FROM current_stocks WHERE stock_symbol = ? AND user_id = ?", stock["symbol"], session["user_id"])
        if current_stock_existence != 0:
            current_stock_count = db.execute("SELECT stock_count FROM current_stocks WHERE stock_symbol = ? AND user_id = ?", stock["symbol"], session["user_id"])
            current_stock_price = db.execute("SELECT price FROM current_stocks WHERE stock_symbol = ? AND user_id = ?", stock["symbol"], session["user_id"])
            db.execute("INSERT INTO current_stocks(stock_name,stock_count,stock_symbol,user_id) VALUES(?,?,?,?)", stock["name"],current_stock_count + request.form.get("numberofshares"), stock["symbol"],session["user_id"])
            db.execute("INSERT INTO stocks_history(stock_name,stock_count,stock_symbol,user_id,time) VALUES(?,?,?,?,datetime(now))", stock["name"], request.form.get("numberofshares"), stock["symbol"], session["user_id"])

        elif:
            db.execute("INSERT INTO current_stocks(stock_name,stock_count,stock_symbol,user_id,price) VALUES(?,?,?,?,?)", stock["name"],request.form.get("numberofshares"), stock["symbol"],session["user_id"])
            db.execute("INSERT INTO stocks_history(stock_name,stock_count,stock_symbol,user_id,time,price) VALUES(?,?,?,?,datetime(now),?)", stock["name"], request.form.get("numberofshares"), stock["symbol"], session["user_id"])

        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

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
    if request.method = "POST":

        #Ensures if stock name is submitted
        if not request.form.get("stockname"):
            return apology("must provide a Stock Name", 403)

        #ensures if stock name is valid
        stock = lookup(request.form.get("stockname"))
        if stock == None:
            return apology("Invalid Stock name", 403)

        return render_template("quoted.html",stock=stock)

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
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        #checks for any existing same username
        if len(rows) != 0:
            return apology("Username already Taken", 403)

        #registers user into database
        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)",request.form.get("username"),generate_password_hash(request.form.get("password")))

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
