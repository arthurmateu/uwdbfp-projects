import datetime
from collections import defaultdict
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
habits = ["Test"]
completions = defaultdict(list)

@app.context_processor
def add_calc_date_range():
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates

    return {"date_range": date_range}

@app.route("/")
def index():
    date_str = request.args.get("date") 
    selected_date = datetime.date.fromisoformat(date_str) if date_str else datetime.date.today()
    return render_template(
        "index.html",
        habits=habits,
        selected_date=selected_date,
        completions=completions[selected_date],
        title="Habit Tracker - Home"
    )


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.form:
        habit = request.form.get("habit")
        if habit:
            habits.append(habit)
    return render_template(
        "add_habit.html",
        title="Habit Tracker - Add Habit",
        # TODO: Find better implementation (add habit in the future/past)
        selected_date=datetime.date.today()
    )


@app.route("/complete", methods=["POST"])
def complete():
    date_string = request.form.get("date")
    habit = request.form.get("habitName")
    # TODO: Find better implementation (it's giving a `Argument of type "str | None" cannot be assigned` warning)
    date = datetime.date.fromisoformat(date_string)
    completions[date].append(habit)

    return redirect(url_for("index", date=date_string))
