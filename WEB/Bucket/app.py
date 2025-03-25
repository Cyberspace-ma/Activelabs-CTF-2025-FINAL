from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

EPISODES_DATA = {
    "red_wedding": {
        "title": "The Rains of Castamere",
        "show": "Game of Thrones",
        "season": 3,
        "episode": 9,
        "description": "One of the most shocking episodes in television history, featuring the infamous Red Wedding.",
        "image": "https://0xy47.s3.us-east-1.amazonaws.com/red-wedding-.jpg",
        "rating": 9.9
    },
    "battle_bastards": {
        "title": "Battle of the Bastards",
        "show": "Game of Thrones",
        "season": 6,
        "episode": 9,
        "description": "Jon Snow and Ramsay Bolton face off in one of the most epic battle sequences ever filmed for television.",
        "image": "https://0xy47.s3.us-east-1.amazonaws.com/Battle-Of-The-Bastards.jpg",
        "rating": 9.9
    },
    "hardhome": {
        "title": "Hardhome",
        "show": "Game of Thrones",
        "season": 5,
        "episode": 8,
        "description": "Jon Snow travels to Hardhome to convince the Free Folk to join forces with the Night's Watch against the White Walkers.",
        "image": "https://0xy47.s3.us-east-1.amazonaws.com/game-of-thrones-hardhome.jpg",
        "rating": 9.8
    },
    "ozymandias": {
        "title": "Ozymandias",
        "show": "Breaking Bad",
        "season": 5,
        "episode": 14,
        "description": "Widely regarded as one of the greatest episodes of television ever made, this episode marks the climax of Walter White's journey.",
        "image": "https://0xy47.s3.us-east-1.amazonaws.com/breaking-bad-ozymandias.jpg",
        "rating": 10.0
    },
    "pine_barrens": {
        "title": "Pine Barrens",
        "show": "The Sopranos",
        "season": 3,
        "episode": 11,
        "description": "Paulie and Christopher get lost in the woods while trying to dispose of what they believe is a dead body.",
        "image": "https://0xy47.s3.us-east-1.amazonaws.com/sopranos-pine-barrens.jpg",
        "rating": 9.7
    },
    "the_constant": {
        "title": "The Constant",
        "show": "LOST",
        "season": 4,
        "episode": 5,
        "description": "Desmond becomes unstuck in time and must find a constant to anchor himself before his consciousness is lost.",
        "image": "https://0xy47.s3.us-east-1.amazonaws.com/LOST-The-Constant.jpg",
        "rating": 9.8
    },
    "the_suitcase": {
        "title": "The Suitcase",
        "show": "Mad Men",
        "season": 4,
        "episode": 7,
        "description": "Don and Peggy pull an all-nighter working on the Samsonite account, leading to profound character development.",
        "image": "https://0xy47.s3.us-east-1.amazonaws.com/Mad-Men-The-Suitcase.jpg",
        "rating": 9.6
    },
    "faith": {
        "title": "Faith",
        "show": "Suits",
        "season": 5,
        "episode": 10,
        "description": "Mike Ross faces the consequences of his actions as his fraud is discovered.",
        "image": "https://0xy47.s3.us-east-1.amazonaws.com/Suits-faiths.jpg",
        "rating": 9.5
    },
    "saul_mike": {
        "title": "Winner",
        "show": "Better Call Saul",
        "season": 4,
        "episode": 10,
        "description": "Jimmy McGill finally embraces his Saul Goodman persona in this pivotal episode.",
        "image": "https://0xy47.s3.us-east-1.amazonaws.com/saul-mike-better-call-saul.jpg",
        "rating": 9.7
    }
}

@app.route('/')
def index():
    return render_template('index.html', episodes=EPISODES_DATA)

@app.route('/episode/<episode_id>')
def episode_detail(episode_id):
    if episode_id in EPISODES_DATA:
        return render_template('episode_detail.html', episode=EPISODES_DATA[episode_id])
    return render_template('404.html'), 404

@app.route('/api/episodes')
def get_episodes():
    return jsonify(EPISODES_DATA)

@app.route('/api/episode/<episode_id>')
def get_episode(episode_id):
    if episode_id in EPISODES_DATA:
        return jsonify(EPISODES_DATA[episode_id])
    return jsonify({"error": "Episode not found"}), 404

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_rating', methods=['POST'])
def submit_rating():
    data = request.json
    episode_id = data.get('episode_id')
    rating = data.get('rating')
    
    if episode_id in EPISODES_DATA and rating is not None:
        return jsonify({"success": True, "message": f"Rating {rating} submitted for {EPISODES_DATA[episode_id]['title']}"})
    
    return jsonify({"error": "Invalid submission"}), 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5301)