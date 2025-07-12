import streamlit as st
import random

# --- Page Setup ---
st.set_page_config(page_title="Rock Paper Scissors vs Zyana", page_icon="🪨", layout="centered")

# --- Emoji Choices ---
choices = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# --- Dynamic Messages ---
win_messages = [
    "🎉 You won! Zyana underestimated you!",
    "🔥 Victory! You beat the bot.",
    "😎 You win this round. Zyana is speechless.",
    "💪 Well played! Zyana couldn't keep up.",
]

lose_messages = [
    "😈 Zyana won! She's learning fast.",
    "💥 Defeated! Try again, human.",
    "🤖 Zyana wins. She’s on a roll!",
    "😬 You lost! Zyana is feeling confident.",
]

draw_messages = [
    "🤝 It's a draw! Great minds think alike.",
    "😐 Tie! Try again.",
    "🌀 A balanced outcome. Let's go again.",
    "🙃 Same move! No winner this time."
]

# --- Leaderboard Setup ---
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = {"Wins": 0, "Losses": 0, "Draws": 0}

def get_winner(player, zyana):
    if player == zyana:
        return "draw"
    elif (
        (player == "Rock" and zyana == "Scissors") or
        (player == "Paper" and zyana == "Rock") or
        (player == "Scissors" and zyana == "Paper")
    ):
        return "user"
    else:
        return "zyana"

# --- Title ---
st.markdown("<h1 style='text-align: center;'>🎮 Rock, Paper, Scissors</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Play against Zyana the AI!</h4>", unsafe_allow_html=True)
st.divider()

# --- Move Selection ---
st.markdown("### 👇 Choose your move:")
user_choice = None
cols = st.columns(3)

for idx, (move, emoji) in enumerate(choices.items()):
    with cols[idx]:
        if st.button(f"{emoji} {move}", use_container_width=True):
            user_choice = move

# --- Game Result Logic ---
if user_choice:
    zyana_choice = random.choice(list(choices.keys()))
    winner = get_winner(user_choice, zyana_choice)

    # Update leaderboard
    if winner == "draw":
        st.session_state.leaderboard["Draws"] += 1
    elif winner == "user":
        st.session_state.leaderboard["Wins"] += 1
    else:
        st.session_state.leaderboard["Losses"] += 1

    st.markdown("---")

    # Show choices
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div style='text-align: center;'>🧍‍♂️<br><b>You:</b><br><span style='font-size:50px'>{choices[user_choice]}</span><br><b>{user_choice}</b></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align: center;'>🤖<br><b>Zyana:</b><br><span style='font-size:50px'>{choices[zyana_choice]}</span><br><b>{zyana_choice}</b></div>", unsafe_allow_html=True)

    st.markdown("---")

    # Show result message
    if winner == "draw":
        st.info(random.choice(draw_messages))
    elif winner == "user":
        st.success(random.choice(win_messages))
    else:
        st.error(random.choice(lose_messages))

    # --- Leaderboard Display ---
    st.markdown("## 🏆 Leaderboard")
    leaderboard = st.session_state.leaderboard

    st.markdown(
        f"""
        <style>
        .leaderboard-table {{
            border-collapse: collapse;
            width: 60%;
            margin: auto;
            font-size: 18px;
            background-color: #f0f2f6;
            color: #000;
            border-radius: 10px;
            overflow: hidden;
        }}
        .leaderboard-table td, .leaderboard-table th {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }}
        .leaderboard-table th {{
            background-color: #e2e4e6;
            font-weight: bold;
        }}
        </style>
        <table class="leaderboard-table">
            <tr>
                <th>🏆 Wins</th><th>😵 Losses</th><th>🤝 Draws</th>
            </tr>
            <tr>
                <td>{leaderboard["Wins"]}</td>
                <td>{leaderboard["Losses"]}</td>
                <td>{leaderboard["Draws"]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True
    )

    # --- Buttons ---
    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        if st.button("🔁 Play Again"):
            st.experimental_rerun()
    with col4:
        if st.button("🗑️ Reset Score"):
            st.session_state.leaderboard = {"Wins": 0, "Losses": 0, "Draws": 0}
            st.experimental_rerun()
