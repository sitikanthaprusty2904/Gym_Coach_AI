import sqlite3
import pathlib as Path
from pathlib import Path
import streamlit as st

_DB_PATH = str(Path(__file__).parent.parent.parent / "data.db")

@st.cache_resource
def _get_connection():
    conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn= _get_connection()

    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS exercises(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL REFERENCES users(id),
                exercise_name TEXT NOT NULL,
                reps INTEGER NOT NULL DEFAULT 0,
                sets INTEGER NOT NULL DEFAULT 0,
                time INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def get_user(username):
    conn=_get_connection()

    return conn.execute("""
        SELECT * FROM users WHERE username = ?
    """, (username,)).fetchone()

def create_user(username):
    conn=_get_connection()

    with conn:
        conn.execute("""
            INSERT INTO users (username) VALUES (?)
        """, (username,))
        return get_user(username)
    
def get_or_create_username(username):
    user=get_user(username)

    if user is None:
        return create_user(username)
    return user


def add_exercise(userid, exercise_name, reps, sets, time):
    conn=_get_connection()

    with conn:
        existing=conn.execute("""
            SELECT * FROM exercises
            WHERE user_id = ? AND exercise_name = ? AND Date(created_at) = Date('now')
        """, (userid, exercise_name)).fetchone()

        if existing:
            conn.execute("""
                UPDATE exercises
                SET reps = reps + ?, sets = sets + ?, time = time + ?
                WHERE id = ?
            """, (reps, sets, time, existing["id"]))
        else:
            conn.execute("""
                INSERT INTO exercises (user_id, exercise_name, reps, sets, time)
                VALUES (?, ?, ?, ?, ?)
            """, (userid, exercise_name, reps, sets, time))
        

def get_users_exercises(userid):
    conn=_get_connection()

    return conn.execute("""
        SELECT * FROM exercises
        WHERE user_id = ? 
    """, (userid,)).fetchall()









