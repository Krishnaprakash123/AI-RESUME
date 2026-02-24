def generate_portfolio(data):
    html_content = f"""
    <html>
    <head><title>{data['name']} Portfolio</title></head>
    <body>
        <h1>{data['name']}</h1>
        <h2>Skills</h2>
        <p>{data['skills']}</p>
        <h2>Projects</h2>
        <p>{data['projects']}</p>
    </body>
    </html>
    """

    with open("portfolio.html", "w") as f:
        f.write(html_content)

    return "portfolio.html"