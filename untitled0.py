# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12IYCjIcWtQfDt5xaPrtlXWCcqnZK57MJ
"""

from IPython.core.display import display, HTML

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Random Joke Generator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      color: #333;
      text-align: center;
      padding: 20px;
    }
    .container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
      background: #fff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    #joke {
      font-size: 1.5em;
      margin: 20px 0;
    }
    button {
      background-color: #007bff;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 1em;
    }
    button:hover {
      background-color: #0056b3;
    }
    .credit {
      margin-top: 20px;
      font-size: 0.9em;
      color: #555;
    }
    .credit a {
      color: #007bff;
      text-decoration: none;
    }
    .credit a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Random Joke Generator</h1>
    <p id="joke">Click the button to get a new joke!</p>
    <button onclick="generateJoke()">Get Joke</button>

    <p class="credit">Tool by <a href="https://menufortexasroadhousewithprices.com" target="_blank">Texas Roadhouse</a></p>
  </div>

  <script>
    const jokes = [
      "Why don’t skeletons fight each other? They don’t have the guts.",
      "What did one ocean say to the other ocean? Nothing, they just waved.",
      "Why did the scarecrow win an award? Because he was outstanding in his field!",
      "Why did the bicycle fall over? Because it was two-tired!",
      "What do you call fake spaghetti? An impasta!",
      "Why couldn’t the leopard hide? Because he was always spotted!",
      "What’s orange and sounds like a parrot? A carrot!",
      "Why don’t eggs tell jokes? They might crack up!",
      "I told my wife she was drawing her eyebrows too high. She looked surprised!",
      "Why did the golfer bring an extra pair of pants? In case he got a hole in one!"
    ];

    function generateJoke() {
      const randomIndex = Math.floor(Math.random() * jokes.length);
      document.getElementById("joke").innerText = jokes[randomIndex];
    }
  </script>
</body>
</html>
"""

display(HTML(html_code))