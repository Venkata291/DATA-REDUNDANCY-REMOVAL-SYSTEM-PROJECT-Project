from flask import Flask, jsonify, render_template
from database import get_connection

app = Flask(__name__)

@app.route('/')
def home():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM employees ORDER BY id"
    )

    employees = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "index.html",
        employees=employees,
        count=len(employees)
    )

@app.route('/remove_duplicates')
def remove_duplicates():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM employees a
        USING employees b
        WHERE a.id > b.id
        AND a.email = b.email
    """)

    deleted = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message":"Duplicates Removed",
        "deleted_records":deleted,
        "remaining_unique_records":5
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
