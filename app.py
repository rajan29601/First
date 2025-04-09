from flask import Flask

app = Flask(__name__)

@app.route("/")
def dashboard():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>DevOps Dashboard</title>
      <style>
        body {
          margin: 0;
          font-family: 'Segoe UI', sans-serif;
          background: #f4f6f9;
        }
        header {
          background-color: #2f3542;
          color: white;
          padding: 20px;
          text-align: center;
        }
        .sidebar {
          height: 100vh;
          width: 220px;
          position: fixed;
          background-color: #1e272e;
          color: #fff;
          padding-top: 30px;
        }
        .sidebar a {
          padding: 15px 25px;
          display: block;
          color: white;
          text-decoration: none;
          transition: 0.3s;
        }
        .sidebar a:hover {
          background-color: #57606f;
        }
        .content {
          margin-left: 240px;
          padding: 30px;
        }
        .card {
          background-color: white;
          padding: 20px;
          margin-bottom: 20px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.1);
          border-radius: 10px;
        }
        .card h2 {
          margin-top: 0;
        }
        .stats {
          display: flex;
          gap: 20px;
        }
        .stat {
          flex: 1;
          background-color: #00a8ff;
          color: white;
          padding: 20px;
          border-radius: 10px;
          text-align: center;
        }
        .stat h3 {
          margin: 0;
          font-size: 24px;
        }
        .stat p {
          margin: 5px 0 0;
        }
      </style>
    </head>
    <body>

      <header>
        <h1>DevOps Dashboard</h1>
      </header>

      <div class="sidebar">
        <a href="#">Overview</a>
        <a href="#">Metrics</a>
        <a href="#">Alerts</a>
        <a href="#">Settings</a>
      </div>

      <div class="content">
        <div class="stats">
          <div class="stat">
            <h3>120</h3>
            <p>Active Servers</p>
          </div>
          <div class="stat" style="background-color: #e84118;">
            <h3>7</h3>
            <p>Incidents Today</p>
          </div>
          <div class="stat" style="background-color: #44bd32;">
            <h3>99.98%</h3>
            <p>Uptime</p>
          </div>
        </div>

        <div class="card">
          <h2>Recent Activity</h2>
          <p>• Server A restarted - 10 mins ago</p>
          <p>• Deployment successful - Project X</p>
          <p>• New alert triggered - High CPU on Node 3</p>
        </div>

        <div class="card">
          <h2>System Notes</h2>
          <p>You can add logs, markdown reports, or links here.</p>
        </div>
      </div>

    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
