#!/usr/bin/env python

"""
Magic 8 ball app.
Designed to be used as an example microservice.
"""

from secrets import choice
from flask import Flask, jsonify
import boto3
import traceback

version = '1.0.45'
app = Flask(__name__)
replies = {
    'positive': [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.'
    ],
    'negative': [
        'Don\'t count on it.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.'
    ],
    'neutral': [
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.'
    ]
}


@app.route("/")
def eightball():
    response = choice(response_pool())
    return jsonify(response)


@app.route("/ping")
@app.route("/ping/<text>")
def ping(text=None):
    return 'PONG {}'.format(text or '').strip()


@app.route("/about")
def about():
    return jsonify({
        'version': version
    })


@app.route("/largest-prime-factor/<num>")
def factorize(num=None):
    # The goal is to be inefficient to push up cpu utilization
    num = int(num)
    i = 2
    while i**2 < num:
        if num % i:
            i += 1
        else:
            num //= i
    return jsonify({
        'prime-factor': num
    })


@app.route("/role")
def role():
    # Test role assumption and print error on failure
    try:
        sts = boto3.client('sts')
        return jsonify(sts.get_caller_identity())
    except Exception:
        return f"<pre>\n{traceback.format_exc()}\n</pre>"


def response_pool():
    return [{'response': reply, 'connotation': category}
            for category in replies for reply in replies[category]]
