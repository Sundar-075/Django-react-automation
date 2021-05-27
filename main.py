import os
import subprocess
from pathlib import Path
name = input("Enter the folder name ")
# name = "dasd"
subprocess.run('django-admin startproject '+name)
present_dir = os.getcwd()
destination_dir = os.path.join(present_dir, name)
os.chdir(destination_dir)
django_commands = ['django-admin startapp api',
                   'django-admin startapp frontend']
for i in django_commands:
    subprocess.run(i)

destination_dir = os.path.join(destination_dir, 'frontend')
os.chdir(destination_dir)
sub_directories = {'src': ['components', 'index.js'],
                   'static': ['css', 'frontend', 'images'], 'templates': 'frontend'}
for i in sub_directories.keys():
    temp_dir = os.path.join(destination_dir, i)
    os.mkdir(temp_dir)
    if i == "src":
        for j in sub_directories[i]:
            if j == "components":
                os.mkdir(temp_dir+"/"+j)
                Path(temp_dir+"/"+j+"/"+"App.js").touch()
                with open(temp_dir+"/"+j+"/"+"App.js", "a") as file:
                    file.write(""" 
                        import React, { Component } from "react";
                        import { render } from "react-dom";

                        export default class App extends Component {
                        constructor(props) {
                            super(props);
                        }
                        render() {
                            return <h1>Hello</h1>;
                        }
                        }
                        const appDiv = document.getElementById("app"); // Index.html Id
                        render(<App />, appDiv); // rendering the above code
                    """.strip())
            else:
                Path(temp_dir+"/"+j).touch()
                with open(temp_dir+"/"+j, "a") as file:
                    file.write(
                        """import App from "./components/App"; """.strip())
    elif i == "static":
        for j in sub_directories[i]:
            if j == "css":
                os.mkdir(temp_dir+"/"+j)
                Path(temp_dir+"/"+j+"/"+"index.css").touch()
            elif j == "frontend":
                os.mkdir(temp_dir+"/"+j)
                Path(temp_dir+"/"+j+"/"+"main.js").touch()
            else:
                os.mkdir(temp_dir+"/"+j)
    else:
        os.mkdir(temp_dir+"/"+sub_directories[i])
        Path(temp_dir+"/"+sub_directories[i]+"/"+"index.html").touch()
        with open(temp_dir+"/"+sub_directories[i]+"/"+"index.html", "a") as file:
            file.write(""" 
                <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>To_do</title>
    {% load static %}
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
    />
    <link
      rel="stylesheet"
      type="text/css"
      href="{% static 'css/index.css' %}"
    />
  </head>
  <body>
    <div id="main">
      <div id="app"></div>
    </div>
    <script src="{% static 'frontend/main.js' %}"></script>
  </body>
</html>
            """.strip())

node_modules = ['npm init -y', 'npm i webpack webpack-cli --save-dev',
                'npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev',
                'npm i react react-dom --save-dev', 'npm install @material-ui/core',
                'npm install @babel/plugin-proposal-class-properties', 'npm install react-router-dom', 'npm install @material-ui/icons']
for cmd in node_modules:
    subprocess.run(cmd, shell=True)

babel_webpack = ['babel.config.json', 'webpack.config.js']
for i in babel_webpack:
    if "babel" in i:
        Path(destination_dir+"/"+i).touch()
        with open(destination_dir+"/"+i, "a") as file:
            file.write("""
                    {
        "presets": [
            [
            "@babel/preset-env",
            {
                "targets": {
                "node": "10"
                }
            }
            ],
            "@babel/preset-react"
        ],
        "plugins": ["@babel/plugin-proposal-class-properties"]
        }
                    """.strip())

    else:
        Path(destination_dir+"/"+i).touch()
        with open(destination_dir+"/"+i, "a") as file:
            file.write("""
            const path = require("path");
            const webpack = require("webpack");

            module.exports = {
            entry: "./src/index.js",
            output: {
                path: path.resolve(__dirname, "./static/frontend"),
                filename: "[name].js",
            },
            module: {
                rules: [
                {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    use: {
                    loader: "babel-loader",
                    },
                },
                ],
            },
            optimization: {
                minimize: true,
            },
            plugins: [
                new webpack.DefinePlugin({
                "process.env": {
                    // This has effect on the react lib size
                    NODE_ENV: JSON.stringify("development"),
                },
                }),
            ],
            };
            """.strip())
with open(destination_dir+"/"+"views.py", "a") as file:
    file.write("""
        from django.shortcuts import render

# Create your views here.


def index(request, *args, **kwargs):
    return render(request, "frontend/index.html")
    """.strip())
