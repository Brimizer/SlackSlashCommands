from flask import Flask, request, Response
from server import app
from server import mongo
import json

@app.route('/pong', methods = ['GET','POST'])
def pong():
    full_command = request.values.get("text")
    print full_command

    command_parts = full_command.split()

    command = command_parts[0]

    if command == 'challenge':
        return challenge_user(request, command_parts)

    elif command == 'leaderboard':
        return show_leaderboard(request, command_parts)

    elif 'winner' in command_parts and 'loser' in command_parts:
        return record_win_loss(request, command_parts)

    return misunderstood(request, command_parts)
        # Error

def challenge_user(request, command_parts):
    user_to_challenge = command_parts[1]

    user_issuing_challenge = request.values.get("user_name")

    response_text = "@" + user_issuing_challenge + " has challenged " + user_to_challenge + " to a death match of Ping Pong!\nPrepare your paddles!"
    standing_text = user_to_challenge + " wins: " + str(10) + " losses: " + str(20)
    response = {'text':response_text, 'attachments':[{'text':standing_text}]}

    return Response(json.dumps(response),  mimetype='application/json')

def show_leaderboard(request, command_parts):
    response = {'text':'Leaderboard'}
    return Response(json.dumps(response),  mimetype='application/json')

def record_win_loss(request, command_parts):
    return Response(json.dumps(response),  mimetype='application/json')

def misunderstood(request, command_parts):
    response = {'text':"Uh-oh! I didn't understand what you meant :("}
    return Response(json.dumps(response),  mimetype='application/json')
