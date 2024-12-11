# COE 550 Course Project - 241 - BI Server

This is a Business Intellegence server running Dash(plotly) framework. It outputs the total number of events per topic.

## How to run the server

First you need to install the following through pip

```bash
pip install dash==2.8.1 pandas==1.5.3 flask flask-restful
```
OR
```bash
pip3 install dash==2.8.1 pandas==1.5.3 flask flask-restful
```

Then to run the server, type the following command
```bash
flask --app app run
```

This exposes `localhost:5000` by default, which is what is configured already from packet tracer side, look for BI Client device in packet tracer.

You don't have to modify anything, just open a web browser on `http://localhost:5000` and keep refreshing the page, the diagram should keep updating this way with new events.